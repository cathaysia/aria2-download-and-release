如果需要下载视频，可以看看我的兄弟项目： [youtube-download and release](https://github.com/cathaysia/youtube-download-and-release) 

# 说明

使用 Github Actions 和 aria2 下载链接发布到 Release

- [x] 多线程下载
- [x] 改善对磁力链接的支持。（感谢 [P3TERX/aria2.conf](https://github.com/P3TERX/aria2.conf)）

# 使用

Fork 这个仓库并向 dl.conf 中添加你需要下载的 URL。一个 URL 占一行。

我使用 rar 对下载的文件进行打包分卷，其目的有两个：

1. Release 单个文件限制为 2GB。本项目将文件分卷为 1.5GB 的压缩包
2. 保护文件名。 release 上传时，特殊字符会被替换掉。（rar 压缩可能会导致文件反而变大）

一次下载的文件总大小不得超过 14GB。


# 注意

如果你已经下载完了，不要忘记把 realses 中的给删掉。请 *善意* 使用 Github 给出的免费空间。

# 鸣谢

- 感谢 Github 对 Action 和 Release 宽松的限制，使得本项目可以实现
- 感谢 aria2 提供的下载器，使得我们可以使用 aria2 去下载喜欢的视频
- 感谢 marvinpinto 提供的 workflow 脚本，使我可以便捷地上传多个 assets
- 感谢 Rar 提供的软件，使我简化了分卷压缩包的创建