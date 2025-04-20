import os
import glob
from datetime import datetime

def read_member_md(path):
    """读取一个成员的 markdown，返回字符串内容（去掉顶层标题）"""
    lines = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('#'):
                continue
            lines.append(line)
    return ''.join(lines)

def build_summary():
    out = []
    
    # 获取当前时间
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # 顶部信息
    out.append('# 小组paper list汇总\n\n')
    out.append('Paper List of the Intelligent Agent Learning Group\n')
    out.append(f'*由 `tools/build_summary.py` 自动生成，请勿手动编辑。*\n')
    out.append(f'*更新时间：{now}*\n\n')

    # 汇总每位成员的内容
    for mdfile in sorted(glob.glob('../papers/*.md', recursive=False), key=lambda x: x.lower()):
        name = os.path.splitext(os.path.basename(mdfile))[0].capitalize()
        out.append(f'## {name}\n\n')
        content = read_member_md(mdfile)
        out.append(content + '\n')

    # 写入目标文件
    target = os.path.join(os.path.dirname(__file__), '..', 'paper_list.md')
    with open(target, 'w', encoding='utf-8') as f:
        f.write(''.join(out))
    
    print(f'✅ 生成完成: {target}')

if __name__ == '__main__':
    build_summary()
