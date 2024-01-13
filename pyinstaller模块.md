# pyinstaller模块



## 一、安装

```bash
pip install pyinstaller==5.10.1

# 建议和我用一样的版本，最新版用法不同
```



## 二、常规用法

```shell
pyinstaller -D run.py -i logo.ico

run.py：要打包的文件/项目入口文件
-D:	打包成多个文件(不指定，默认就是打包成多个文件)
-F:	打包成一个单独的文件(如果你的代码都写在一个py文件的话，就可以用这个，如果是多个py文件就别用这个)
-w: 程序运行时不显示命令行窗口（仅对 Windows 有效）
-i logo.ico：指定图标文件路径，必须是ico格式


# 如果图标没能及时刷新显示的解决方法，在cmd终端敲以下命令：
Win10：ie4uinit.exe -show
Win7/Win8：ie4uinit.exe -ClearIconCache
```



## 三、进阶用法

1. 生成spec配置文件

   ```shell
   pyi-makespec run.py
   
   # 执行完这条命令之后，会在当前工作目录产生一个run.spec的配置文件
   ```

   

2. 配置spec

   ```python
   # 在配置文件里配置这两项即可
   
   # 1、需要打包的依赖文件（'源地址','目标地址'）
   a = Analysis(
   	    datas=[('settings.cfg','.'),('db\\goods_data','db\\goods_data'),('db\\user_data','db\\user_data'),('log','log')],
   )
   
   # 2、指定打包之后的可执行文件的图标（也可以不指定图标）
   exe = EXE(
       icon='imgs\\logo.ico',
       console=True,	# 此参数默认为True, 如果程序运行的时候不需要显示命令行窗口，则可以改成False，改成False之后，则和前面常规用法里面的-w效果一样，只是我们现在必须依赖命令行窗口和用户交互，所以不用改它，默认就好。
   )
   
   # 3、防止打包的exe被反编译(abc123是加密密钥，可以随意更换，类似哈希加盐)
   # 此加密参数依赖第三方模块tinyaes，需要安装：pip install tinyaes
   block_cipher = pyi_crypto.PyiBlockCipher(key='abc123')
   ```

   

3. 打包

   ```shell
   pyinstaller run.spec
   ```

   

4. 以上三步，也可并为以下一步

   ```shell
   pyinstaller run.py -i imgs\logo.ico --key abc123 --add-data "settings.cfg;." --add-data "db\goods_data;db\goods_data" --add-data "db\user_data;db\user_data" --add-data "log;log"
   
   
   -i imgs\logo.ico	# 指定图标文件路径，必须是ico格式
   --key abc123	# 防止打包的exe被反编译(abc123是加密的密钥，可以随意更换，类似哈希加盐)
   --add-data "源地址;目标地址"  # windows以;分割，linux以:分割
   ```

   

<p align="right"><a href="https://v.ixigua.com/2asfSbf/">@author:小飞有点东西</a></p><p align="right"><a href="https://active.clewm.net/FrcyFA">点我获取更多资料</a></p>

