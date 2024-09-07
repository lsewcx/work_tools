# 贡献指南

## 启动项目

### 克隆项目

首先，克隆项目到本地：

```bash
git clone https://github.com/lsewcx/work_tools.git
cd work_tools
```

### 安装

使用 conda 创建一个 python3.9 版本的环境

```bash
pip install -U poetry
poetry install -v
```

如果你需要添加库请使用

```bash
poetry add [库名字]
```

## 贡献

### 写完代码后在项目根目录运行 isort 对导入进行格式化

```bash
isort .
```

### 在项目根目录运行 pylint 检查代码是否规范，是否符合 PEP8 标准。

```bash
pylint tests src
```

### 进行测试知道代码没有问题了

```bash
pytest
```

### 文档

如果你添加的是新功能，编写 markdown 文件参照别的 markdown 的标准会通过函数的注释自动生成文档

### 上传

```bash
git cz
git push
```

## 常见问题

### windows 平台

经过测试 mac 平台可以直接输入

```bash
mkdocs serve
```

windows 平台如果无效请使用

```bash
poetry run mkdocs serve
```
