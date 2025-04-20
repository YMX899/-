import os
import glob

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
    out.append('# 团队论文总 Paper list :facepunch:\n\n')
    out.append('=====================\n')
    out.append('Paper List of the Intelligent Agent Learning Group\n')
    out.append('*由 `tools/build_summary.py` 自动生成，请勿手动编辑。*\n\n')

    for mdfile in sorted(glob.glob('../papers/*.md', recursive=False), key=lambda x: x.lower()):
        name = os.path.splitext(os.path.basename(mdfile))[0].capitalize()
        out.append(f'## {name}\n\n')
        content = read_member_md(mdfile)
        out.append(content + '\n')

    target = os.path.join(os.path.dirname(__file__), '..', 'paper_list.md')
    with open(target, 'w', encoding='utf-8') as f:
        f.write(''.join(out))
    print(f'✅ 生成完成: {target}')

if __name__ == '__main__':
    build_summary()
