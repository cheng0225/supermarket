# supermarket
改成django的sqlite数据库版本，方便部署到pythonanywhere

内置了虚拟环境    
在supermarket根目录下执行如下两条命令即可食用
进入虚拟环境（windows） `activate venv`   
启动运行django `python manage.py runserver`

前端运行 `npm run dev`   
前端打包 `npm run build`   
前端环境配置 `supermarketqd/src/util/request.js`   

git部分   
切换分支 `git checkout branchName`    
创建新分支并切换 `git checkout -b newBranch`   
等同于下面两句
```
git branch newBranch
git checkout newBranch
```
