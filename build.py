"""Create the standalone catalogue from two explicit release files; never execute EJS."""
from pathlib import Path
from datetime import datetime
import argparse, json, base64, shutil, hashlib

HERE = Path(__file__).resolve().parent
parser=argparse.ArgumentParser()
parser.add_argument('--worldbook',type=Path,required=True)
parser.add_argument('--quickreply',type=Path,required=True)
parser.add_argument('--sources',type=Path)
args=parser.parse_args()
book=json.loads(args.worldbook.read_text())
qr=json.loads(args.quickreply.read_text())

def array(content,marker):
 return json.JSONDecoder().raw_decode(content.split(marker,1)[1].lstrip())[0]

catalog=[]
themes=[('occult','密教','密教与司辰之书','梦、准则与漫宿','◇','#986b32'),
        ('coc','COC','克苏鲁神话','秘术、幻梦与异界','◉','#557f70'),
        ('dnd','DND','龙与地下城','职业、法术与诸位面','✧','#72679a'),
        ('warhammer','战锤40K','战锤 40,000','灵能、超人与遥远未来','✣','#986254')]
for offset,(sid,short,title,desc,symbol,color) in enumerate(themes):
 p=book['entries'][str(1+offset*2)]['content']
 q=book['entries'][str(2+offset*2)]['content']
 levels=array(p,'const levels=')
 lore=array(p,'const records=')
 items=array(q,'const items=')
 core=array(p,'\nconst core=') if '\nconst core=' in p else array(p,'if(active){\nprint(')
 races=array(p,'const races=') if sid=='dnd' and 'const races=' in p else []
 if races:
  levels=[dict(r, key='DND·'+race['name']+'·'+r['career']+'·'+r['rank'],
      race=race['name'],raceBody=race['body'],baseBody=r['body'],
      menuPath=['DND','等级',race['name'],r['career'],r['rank']],
      body=r['body']+'\n\n【种族：'+race['name']+'】\n'+race['body'])
      for race in races for r in levels]
 def level_group(r):
  return ' / '.join(r['menuPath'][2:4]) if sid=='coc' and r.get('menuPath') else r['career']
 groupLevels=list(dict.fromkeys(level_group(r) for r in levels))
 groupItems=list(dict.fromkeys(k.split('·')[1] for r in items for k in r['keys']))
 records=[]
 for i,r in enumerate(levels):
  records.append(dict(id=f'{sid}-level-{i}',kind='level',name=r['rank'],group=level_group(r),groups=[level_group(r)],
      key=r['key'],category=r.get('category',''),menuPath=r.get('menuPath',[]),
      race=r.get('race',''),raceBody=r.get('raceBody',''),baseBody=r.get('baseBody',''),
      grade=r['defaultGrade'],rating=r['rating'],body=r['body'],keyword='我的力量：【'+r['key']+'】',
      lore=[lore[j] for j in r['sections']],sources=r.get('sources',[]),revision=r.get('revision',''),updatedAt=r.get('updatedAt','')))
 for i,r in enumerate(items):
  records.append(dict(id=f'{sid}-item-{i}',kind='item',name=r['title'],group=r['keys'][0].split('·')[1],
      groups=list(dict.fromkeys(k.split('·')[1] for k in r['keys'])),grade=r['defaultGrade'],rating=r['rating'],
      body=r['body'],keyword='持有道具：【'+r['keys'][0]+'】',lore=[],sources=r.get('sources',[]),source=r.get('source',''),revision=r.get('revision',''),updatedAt=r.get('updatedAt','')))
 catalog.append(dict(id=sid,short=short,title=title,description=desc,symbol=symbol,color=color,
                     core=core,races=[r['name'] for r in races],
                     groupLevels=groupLevels,groupItems=groupItems,records=records))

for group in catalog:
 missing=[r['id'] for r in group['records'] if not r['body'].startswith('【战斗力】'+r['grade']+'（')]
 if missing:
  raise ValueError('待发布条目缺少战斗力短句或档位不一致：'+', '.join(missing))
 print(group['short']+'：'+str(len(group['records']))+'项，战斗力短句全部齐全。')

downloads=[]
for src,label in [(args.worldbook,'世界书'),(args.quickreply,'快速回复')]:
 dest=HERE/'downloads'/src.name
 shutil.copy2(src,dest)
 downloads.append(dict(name=src.name,label=label,version=book['version'] if label=='世界书' else qr['name'].replace('自用力量体系_v','').replace('_','.'),
                       base64=base64.b64encode(src.read_bytes()).decode(),size=round(src.stat().st_size/1024)))
data=dict(version=book['version'],catalog=catalog,downloads=downloads,license=book.get('license',''),
          general=book['entries']['0']['content'],repo='https://github.com/LoraineConleyxxy/power-atlas',
          grades=['爆砖','爆墙','爆屋','爆楼','爆街','爆城','爆国','大陆','地表','爆星','恒星','星系','宇宙结构','单体宇宙','多元','无限多元','高阶多元','无限盒子及更高迭代','指数塔','超指数塔','论外'])
data['sources']=json.loads(args.sources.read_text()).get('sources',{}) if args.sources else {}
data['updatedAt']=book.get('updatedAt',datetime.now().astimezone().isoformat(timespec='seconds'))
data['buildId']=hashlib.sha256(args.worldbook.read_bytes()+args.quickreply.read_bytes()+(HERE/'src/index.template.html').read_bytes()+Path(__file__).read_bytes()).hexdigest()[:12]
retained={f['name'] for f in downloads}
for old in (HERE/'downloads').glob('_自用力量体系*.json'):
 if old.name not in retained: old.unlink()
embedded=json.dumps(data,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c')
template=(HERE/'src/index.template.html').read_text()
html=template.replace('__CATALOG_DATA__',embedded)
(HERE/'index.html').write_text(html)
reviewName='review-v'+book['version']+'.html'
(HERE/reviewName).write_text(html)
for old in HERE.glob('review-v*.html'):
 if old.name!=reviewName:old.unlink()
(HERE/'release.json').write_text(json.dumps(dict(version=data['version'],updatedAt=data['updatedAt'],buildId=data['buildId'],url=reviewName),ensure_ascii=False)+'\n')
(HERE/'.nojekyll').touch()
print('已生成独立展示页与两个下载文件。')
