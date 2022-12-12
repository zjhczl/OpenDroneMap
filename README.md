- [OpenDroneMap](#opendronemap)
  - [1. ODM](#1-odm)
    - [1.1. 简介](#11-简介)
    - [1.2. 安装ODM](#12-安装odm)
      - [1.2.1. 使用Docker安装](#121-使用docker安装)
      - [1.2.2. windows本地安装](#122-windows本地安装)
      - [1.2.3. Ubuntu本地安装](#123-ubuntu本地安装)
      - [1.2.4. MacOS本地安装](#124-macos本地安装)
  - [2. NodeODM](#2-nodeodm)
    - [2.1. 简介](#21-简介)
    - [2.2. 安装NodeODM](#22-安装nodeodm)
      - [2.2.1. Docker运行NodeODM](#221-docker运行nodeodm)
      - [2.2.2. 本机运行NodeODM](#222-本机运行nodeodm)
  - [3. WebODM](#3-webodm)
    - [3.1. 简介](#31-简介)
    - [3.2. 安装WebODM](#32-安装webodm)
      - [3.2.1. Docker安装WebODM](#321-docker安装webodm)





# OpenDroneMap

OpenDroneMap项目由几个组件组成：

ODM是一个处理航拍图像的命令行工具包。熟悉命令行的用户可能可以单独使用此组件。

NodeODM是直接构建在ODM之上的轻量级接口和 API（应用程序接口）。不习惯命令行的用户可以使用此接口处理航拍图像，开发人员可以使用 API 构建应用程序。不提供用户身份验证、地图显示等功能。

WebODM添加了更多功能，例如用户身份验证、地图显示、3D 显示、更高级别的 API 以及编排多个处理节点（并行运行作业）的能力。处理节点只是运行NodeODM 的服务器。

## 1. ODM

### 1.1. 简介

用于处理航空无人机图像的开源命令行工具包。ODM 将简单的 2D 图像转换为：
    -分类点云
    -3D 纹理模型
    -地理参考正射影像
    -地理参考数字高程模型
文档:https://docs.opendronemap.org/
### 1.2. 安装ODM
#### 1.2.1. 使用Docker安装
运行 ODM 的最简单方法是通过 docker。

可以通过将一些图像（JPEG 或 TIFF）放入名为“images”（例如C:\Users\youruser\datasets\project\images或/home/youruser/datasets/project/images）的文件夹中来运行 ODM，然后只需从命令提示符/终端运行：

```bash
# Windows
docker run -ti --rm -v c:/Users/youruser/datasets:/datasets opendronemap/odm --project-path /datasets project

# Mac/Linux
docker run -ti --rm -v /home/youruser/datasets:/datasets opendronemap/odm --project-path /datasets project
```

可以通过将附加参数附加到命令来传递附加参数：

```bash
docker run -ti --rm -v /datasets:/datasets opendronemap/odm --project-path /datasets project [--additional --parameters --here]
```

例如，要生成 DSM ( --dsm) 并增加正射影像分辨率 ( --orthophoto-resolution 2) ：

```bash
docker run -ti --rm -v /datasets:/datasets opendronemap/odm --project-path /datasets project --dsm --orthophoto-resolution 2
```

#### 1.2.2. windows本地安装

网址：https://github.com/OpenDroneMap/ODM/releases
ODM 可以本地安装在 Windows 上。打开 ODM 控制台后，您可以通过键入以下内容来处理数据集：
```bash
run C:\Users\youruser\datasets\project  [--additional --parameters --here]
```

#### 1.2.3. Ubuntu本地安装

```bash
git clone https://github.com/OpenDroneMap/ODM
cd ODM
bash configure.sh install
```

然后你可以处理数据集

```bash
./run.sh /datasets/odm_data_aukerman
```

#### 1.2.4. MacOS本地安装
需要先安装 Xcode 13 和 Homebrew
```bash
git clone https://github.com/OpenDroneMap/ODM
cd ODM
bash configure_macos.sh install
```

然后你可以处理数据集

```bash
./run.sh /datasets/odm_data_aukerman
```

## 2. NodeODM

### 2.1. 简介
NodeODM 是一种标准的 API 规范，用于使用ODM等引擎处理航拍图像。该 API 由WebODM、CloudODM和PyODM等客户端使用。

文档:https://github.com/OpenDroneMap/NodeODM/blob/master/docs/index.adoc
### 2.2. 安装NodeODM

#### 2.2.1. Docker运行NodeODM

从 Docker 快速启动终端 (Windows / OSX) 或从命令行 (Linux) 键入：

```bash
docker run -p 3000:3000 opendronemap/nodeodm
```

如果要将结果存储在单独的驱动器上，请将/var/www/data文件夹映射到驱动器的位置：

```bash
docker run -p 3000:3000 -v /mnt/external_hd:/var/www/data opendronemap/nodeodm
```
#### 2.2.2. 本机运行NodeODM
如果您已经在 Ubuntu 上本地运行ODM ，您可以按照以下步骤操作：

安装 Entwine： https: //entwine.io/quickstart.html#installation

安装 node.js、npm 依赖、7zip 并解压：

```bash
sudo curl --silent --location https://deb.nodesource.com/setup_6.x | sudo bash -
sudo apt-get install -y nodejs python-gdal p7zip-full unzip
git clone https://github.com/OpenDroneMap/NodeODM
cd NodeODM
npm install
```

启动NodeODM
```bash
node index.js
```
您可能需要指定 ODM 项目路径以启动服务器：

```bash 
node index.js --odm_path /home/username/OpenDroneMap
```

如果你想在不同的端口上启动节点 ODM，你可以执行以下操作：

```bash
node index.js --port 8000 --odm_path /home/username/OpenDroneMap
```

对于其他命令行选项，您可以运行：

```bash
node index.js --help
```
## 3. WebODM

### 3.1. 简介

WebODM相当于为ODM提供了UI界面，它仍然可以从航拍图像生成地理参考地图、点云、高程模型和带纹理的 3D 模型。
文档：http://docs.webodm.org/#introduction

### 3.2. 安装WebODM

#### 3.2.1. Docker安装WebODM
安装WebODM前，需在在计算机安装如下的软件：
Git
Docker
Docker-compose
Python
Pip

从 Docker 快速启动终端或 Git Bash (Windows)，或从命令行 (Mac / Linux)，键入：

```bash
git clone https://github.com/OpenDroneMap/WebODM --config core.autocrlf=input --depth 1
cd WebODM
./webodm.sh start 
```
打开 Web 浏览器http://localhost:8000

使用 Docker 时，所有处理结果都存储在 docker 卷中，并且在主机文件系统上不可用。如果要将文件存储在主机文件系统而不是 docker 卷上，则需要通过以下选项传递路径--media-dir：

```bash
./webodm.sh restart --media-dir /home/user/webodm_data
```
<!-- 
#### 3.2.2. 本机安装WebODM

本机器安装WebODM前需要先安装如下软件:
PostgreSQL (>= 9.5)
PostGIS 2.3
Python 3.6
GDAL (>= 3)
Node.js (>= 6.0)
Nginx (Linux/MacOS) - OR - Apache + mod_wsgi or Waitress (Windows)
Redis (>= 2.6)
GRASS GIS (>= 7.8)

在 Linux 上，确保你有：

```bash
apt-get install binutils libproj-dev gdal-bin nginx
```

在 Windows 上使用<a href="https://trac.osgeo.org/osgeo4w">OSGeo4W</a>安装程序安装 GDAL。MacOS 用户可以使用：

```bash
brew install postgres postgis
``` -->
