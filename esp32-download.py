#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os
import subprocess

JSON_FILE = 'package_esp32_index_cn.json'

SYS_LIST = [
    'windows-32',
    'windows-64',
    'linux-64',
    'linux-32',
    'linux-arm64',
    'linux-armv7',
    'macos-x86_64',
    'macos-arm64',
]

SYS_MAP = {
    'windows-32': 'i686-mingw32',
    'windows-64': 'x86_64-mingw32',
    'linux-64': 'x86_64-pc-linux-gnu',
    'linux-32': 'i686-pc-linux-gnu',
    'linux-arm64': 'aarch64-linux-gnu',
    'linux-armv7': 'arm-linux-gnueabihf',
    'macos-x86_64': 'x86_64-apple-darwin',
    'macos-arm64': 'arm64-apple-darwin',
}

def load_index():
    if not os.path.isfile(JSON_FILE):
        print(f'当前目录未找到 {JSON_FILE}，请把文件放到本脚本同级目录')
        exit(1)
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_versions(data):
    versions = set()
    for pkg in data['packages']:
        if pkg['name'] == 'esp32':
            for pf in pkg['platforms']:
                versions.add(pf['version'])
    return sorted(versions, reverse=True)

def build_tools_dict(data):
    tools = {}
    for t in data['packages'][0]['tools']:
        key = (t['name'], t['version'])
        tools[key] = t['systems']
    return tools

def pick_cn_url(systems, host):
    for s in systems:
        if s['host'] == host and s['url'].startswith('https://dl.espressif.cn/'):
            return s['url']
    return None

def download(url: str):
    filename = url.split('/')[-1]
    if subprocess.call(['wget', '-q', '--show-progress', '-O', filename, url]) == 0:
        return
    if subprocess.call(['curl', '-L', '-o', filename, url]) == 0:
        return
    print(f'下载失败：{url}')

def main():
    data = load_index()
    versions = get_versions(data)

    print('请选择 ESP32 版本：')
    for idx, ver in enumerate(versions, 1):
        print(f'  {idx}. {ver}')
    try:
        ver_idx = int(input('输入序号：')) - 1
        version = versions[ver_idx]
    except (ValueError, IndexError):
        print('选择无效')
        exit(1)

    print('\n请选择系统版本：')
    for idx, sys in enumerate(SYS_LIST, 1):
        print(f'  {idx}. {sys}')
    try:
        sys_idx = int(input('输入序号：')) - 1
        sys_key = SYS_LIST[sys_idx]
        host = SYS_MAP[sys_key]
    except (ValueError, IndexError):
        print('选择无效')
        exit(1)

    pf = next(p for p in data['packages'][0]['platforms'] if p['version'] == version)
    tools_map = build_tools_dict(data)

    downloads = []
    if pf.get('url', '').startswith('https://dl.espressif.cn/'):
        downloads.append(('esp32-platform', pf['url']))

    for dep in pf['toolsDependencies']:
        name, ver_tool = dep['name'], dep['version']
        systems = tools_map.get((name, ver_tool))
        if not systems:
            continue
        url = pick_cn_url(systems, host)
        if url:
            downloads.append((name, url))

    if not downloads:
        print('未找到任何 dl.espressif.cn 的下载地址')
        exit(0)

    print('\n找到以下可下载项：')
    for name, url in downloads:
        print(f'  {name} : {url}')

    confirm = input('\n是否开始下载？输入 Y 确认：').strip().lower()
    if confirm != 'y':
        print('已取消下载')
        exit(0)

    os.makedirs(version, exist_ok=True)
    os.chdir(version)

    for name, url in downloads:
        print(f'正在下载 {name} ...')
        download(url)

    print('全部下载完成！')

if __name__ == '__main__':
    main()
