# Starting the Skeleton Driver

2019-05-21 · https://fsgeek.ca/log/starting-the-skeleton-driver/

![](https://i2.wp.com/fsgeek.ca/wp-content/uploads/2019/05/VS19-start-driver.png?fit=600%2C400&ssl=1)Screen shot of my newly created skeleton driver

[In my last post](https://fsgeek.ca/wp-admin/post.php?post=641), I installed the WDK (and described why I want to build a file system driver). I started up Visual Studio 2019, said I wanted to create a new project, narrowed down the options to "WDK" related projects, and scrolled down to the WDM driver option.

I'm not building a WDM driver, but it is the closest project type to what I want to do. It creates a _solution_ with the name specified and then creates a _project_ with the same name. The only file that it pre-constructs for me is an **inf** file. I will need to do work on that before I can use it, but I'll leave that for later. File system installation files are surprisingly uncomplicated, since all we really need to do to install a file system driver is set up a few registry keys.

Since I had just installed Visual Studio 2019, I'll need to tune things to my working environment. I started by enabling git integration, since I will be using github.com for my source code repository ([winskel](https://github.com/fsgeek/winskel)).

That took more time than I anticipated - I installed the Github integration into Visual Studio, which restarted Visual Studio. I was then told "there is an update to GitHub extension for Visual Studio". Thus, I installed the update next. That required another restart to install the update. I hope the Visual Studio folks take a lesson from the VS Code team, since I install VS Code extension updates all the time with just a refresh, not a full restart. Of course, I used that time to continue adding to my post here, so it wasn't _entirely_ wasted time. Still, it is stunning that they construct a restore point just for installing new extensions.  


![](https://i1.wp.com/fsgeek.ca/wp-content/uploads/2019/05/disable-wdk-extensions-warning.png?fit=600%2C21&ssl=1)The new helpful error message upon restarting!

I really liked the fact that Visual Studio 2019 suggested to me that I could make startup faster by _disabling_ the WDK extension - how _helpful_ , given that the reason I'm running Visual Studio 2019 is because I want to use the WDK. It makes me long for the days of SOURCES files and command line program building. I know it is possible to develop without using Visual Studio and perhaps I'll explore that again at some point, but I'd rather be writing code for my new driver rather than fussing with the tools and environment at this point.

![](https://i2.wp.com/fsgeek.ca/wp-content/uploads/2019/05/code-analysis.png?fit=600%2C428&ssl=1)I enable code analysis - it can be annoying, but it also finds bugs.

Since this is a new project, I'm going to enable the static code analysis tools. While not _required_ , I choose the "All Rules" option because it is the most restrictive setting available. Note that I am applying this to all the configurations (debug and release) as well as the platforms for which I have installed the compiler tools (I did not install the ARM compiler tools, so I cannot include them).

Having enabled the checks, I built my simple file with just **DriverEntry** (and an error return). Of course, as I expected, the static analysis tools are now reporting issues, so I add annotations (**DRIVER_INITIALIZE DriverEntry;** for example) and modify my code (the static analyzer points out that both the **DriverObject** and **RegistryPath** can be set as **const** pointers). Since I will be changing **DriverObject** I suppress the warning. I don't expect to change the **RegistryPath** , so I mark it as **const**.

I also had a warning that while the spectre/meltdown mitigation option has been selected for the compiler, the libraries with the needed mitigations are not installed. So back I went into the installer and installed the missing libraries. Things now build well, and I have my super-minimal driver. It won't **do** much, since the **DriverEntry** function returns a failure code, which means it will load and then unload.

However, this is enough for me to make the **inf** file work, so I will do that next.

![](/media/2019/05/winskel.inf_.png)This is the default INF file that Visual Studio provided to me.  
  


Visual Studio generated a default INF file for me. This isn't _quite_ enough for me to install a working driver, so I'll need to modify it. Plus, Microsoft changed some details about INF files for Windows 10 1903 and created a new _[primitive](https://docs.microsoft.com/en-us/windows-hardware/drivers/develop/creating-a-primitive-driver)_[ driver ](https://docs.microsoft.com/en-us/windows-hardware/drivers/develop/creating-a-primitive-driver)type with rules that need to be followed if you want the driver to be properly (test) signed.

So I worked through the INF file issues and I now have a working INF file, with a driver that (of course) won't actually _do_ anything yet.

Next, I turned my attention to pulling together a C++ runtime so that I _can_ use C++ if I want. Basically, there are several things that need to be done to make this work:

  * I need memory management functions
  * I need initializer support
  * I have to wrap the standard functionality (DriverEntry) and coordinate the Unload function so it calls the cleanup logic.



In the past, I've added a template layer above the allocators, which permits me to specify (on a per-object type) what the pool type and pool tag are for the allocations. Unlike in user mode memory, where we normally don't worry about these things, in the kernel we _do_ need to worry about whether memory is pageable or not. Plus, we have to provide some mechanism for finding memory leaks since there is no automatic garbage collection. Note that my goal isn't to port STL into the Windows kernel (though I _did_ see one project where it looked like someone had done that). Similarly, I don't plan on supporting C++ structured exception handling. So it will provide me with most C++ code features, but I'll eschew those that require specialized run-time support.

As I wrap this up for the day, I have the allocation routines plumbed. The next step is to get the initializer code written - it revolves around walking through some memory locations where global and static constructors need to be called - the Microsoft C++ compiler embeds some magic information in memory to do this. I also need to construct a list of things to be called when terminating the runtime.

Once that's done, I'll move on to adding basic functionality. One thing that will greatly simplify this initial effort is that I don't have to worry about integration with the memory manager or cache manager because I can defer I/O management to the native file system. Perhaps, once we've proven the viability of this approach, I can look further at integration.

I will continue describing my progress and updating the repository as I work through this project over the coming months.
