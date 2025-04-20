# paper-hub :rocket:
===========                                          
Paper List of the Intelligent Agent Learning Group

### 介绍
本仓库用于汇总小组成员的阅读笔记和团队总表。
- `papers/`：这个文件夹存放着每人单独的 Markdown 笔记，大家只需要编辑属于自己名字的笔记即可。
- `paper_list.md`：为了方便阅读和检索而设置此汇总后的团队总表，平时可以直接阅读此汇总表。此由脚本自动生成。大家需要在完成自己markdown记录后，运行`tools/build.bat`脚本，这个脚本将会更新`paper_list.md`，将所有人的paper list合并到`paper_list.md`。
- `tools/build.py`：存放汇总生成的脚本
### 使用方法
1. 首次使用先安装好Git环境
2. 首先PULL代码到本地
3. 大家在 `papers/yourname.md` 中按模板填写论文清单 ，如果属于自己的`yourname.md`,请自行创建
4. 运行 `tools/build.bat` 生成最新的 `paper_list.md`
5. 检查修改，然后PUSH

:bulb: **Tip**  yourname.md的书写方法和格式在 
``` 
paper-hub/example.md        
```
:star2: **注意事项**
- **环境**
首先推荐Vscode+Git for Windows进行操作。其次请安装Python环境再运行脚本，否则脚本将无法正常运行。

- **合并脚本**
其实不运行脚本，只修改自己的MD文件，请小伙伴帮忙合并也是可以的 :stuck_out_tongue_winking_eye:
- **谨慎修改**
为了使用方便，目前暂未开启PR和Review，也就是说，你的Push会直接合并。所以，千万不要修改除了 `yourname.md`之外的任何文件，可能导致仓库出现灾难性错误。
（不过其实只要你只修改`yourname.md`和运行脚本就不会出错:smile:）
- **Commit要求**
请带上如250420-lihua这样的信息进行Commit，以方便大家追踪更新记录
- **其他**
欢迎补充



