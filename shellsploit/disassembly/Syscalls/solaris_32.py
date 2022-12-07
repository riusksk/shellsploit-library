#------------------Bombermans Team------------------------------------------# 
# Author  : B3mB4m
# Concat  : b3mb4m@protonmail.com
# Project : https://github.com/b3mb4m/shellsploit-library
# LICENSE : https://github.com/b3mb4m/shellsploit-library/blob/master/LICENSE
#----------------------------------------------------------------------------#


def SolarisSystemcall( sys, key=None):
    list = {
        "syscall":"0",
        "exit":"1",
        "forkall":"2",
        "read":"3",
        "write":"4",
        "open":"5",
        "close":"6",
        "wait":"7",
        "creat":"8",
        "link":"9",
        "unlink":"10",
        "exec":"11",
        "chdir":"12",
        "time":"13",
        "mknod":"14",
        "chmod":"15",
        "chown":"16",
        "brk":"17",
        "stat":"18",
        "lseek":"19",
        "getpid":"20",
        "mount":"21",
        "umount":"22",
        "setuid":"23",
        "getuid":"24",
        "stime":"25",
        "pcsample":"26",
        "alarm":"27",
        "fstat":"28",
        "pause":"29",
        "utime":"30",
        "stty":"31",
        "gtty":"32",
        "access":"33",
        "nice":"34",
        "statfs":"35",
        "sync":"36",
        "kill":"37",
        "fstatfs":"38",
        "pgrpsys":"39",
        "uucopystr":"40",
        "dup":"41",
        "pipe":"42",
        "times":"43",
        "profil":"44",
        "plock":"45",
        "setgid":"46",
        "getgid":"47",
        "signal":"48",
        "msgsys":"49",
        "sysi86":"50",
        "acct":"51",
        "shmsys":"52",
        "semsys":"53",
        "ioctl":"54",
        "uadmin":"55",
        "utssys":"57",
        "fdsync":"58",
        "execve":"59",
        "umask":"60",
        "chroot":"61",
        "fcntl":"62",
        "ulimit":"63",
        "reserved_64":"64",
        "reserved_65":"65",
        "reserved_66":"66",
        "reserved_67":"67",
        "reserved_68":"68",
        "reserved_69":"69",
        "tasksys":"70",
        "acctctl":"71",
        "exacctsys":"72",
        "getpagesizes":"73",
        "rctlsys":"74",
        "sidsys":"75",
        "fsat":"76",
        "lwp_park":"77",
        "sendfilev":"78",
        "rmdir":"79",
        "mkdir":"80",
        "getdents":"81",
        "privsys":"82",
        "ucredsys":"83",
        "sysfs":"84",
        "getmsg":"85",
        "putmsg":"86",
        "poll":"87",
        "lstat":"88",
        "symlink":"89",
        "readlink":"90",
        "setgroups":"91",
        "getgroups":"92",
        "fchmod":"93",
        "fchown":"94",
        "sigprocmask":"95",
        "sigsuspend":"96",
        "sigaltstack":"97",
        "sigaction":"98",
        "sigpending":"99",
        "context":"100",
        "evsys":"101",
        "evtrapret":"102",
        "statvfs":"103",
        "fstatvfs":"104",
        "getloadavg":"105",
        "nfssys":"106",
        "waitid":"107",
        "waitsys":"SYS_waitid",
        "sigsendsys":"108",
        "hrtsys":"109",
        "sigresend":"111",
        "priocntlsys":"112",
        "pathconf":"113",
        "mincore":"114",
        "mmap":"115",
        "mprotect":"116",
        "munmap":"117",
        "fpathconf":"118",
        "vfork":"119",
        "fchdir":"120",
        "readv":"121",
        "writev":"122",
        "xstat":"123",
        "lxstat":"124",
        "fxstat":"125",
        "xmknod":"126",
        "setrlimit":"128",
        "getrlimit":"129",
        "lchown":"130",
        "memcntl":"131",
        "getpmsg":"132",
        "putpmsg":"133",
        "rename":"134",
        "uname":"135",
        "setegid":"136",
        "sysconfig":"137",
        "adjtime":"138",
        "systeminfo":"139",
        "sharefs":"140",
        "seteuid":"141",
        "forksys":"142",
        "fork1":"143",
        "sigtimedwait":"144",
        "lwp_info":"145",
        "yield":"146",
        "lwp_sema_wait":"147",
        "lwp_sema_post":"148",
        "lwp_sema_trywait":"149",
        "lwp_detach":"150",
        "corectl":"151",
        "modctl":"152",
        "fchroot":"153",
        "utimes":"154",
        "vhangup":"155",
        "gettimeofday":"156",
        "getitimer":"157",
        "setitimer":"158",
        "lwp_create":"159",
        "lwp_exit":"160",
        "lwp_suspend":"161",
        "lwp_continue":"162",
        "lwp_kill":"163",
        "lwp_self":"164",
        "lwp_sigmask":"165",
        "lwp_private":"166",
        "lwp_wait":"167",
        "lwp_mutex_wakeup":"168",
        "lwp_mutex_lock":"169",
        "lwp_cond_wait":"170",
        "lwp_cond_signal":"171",
        "lwp_cond_broadcast":"172",
        "pread":"173",
        "pwrite":"174",
        "llseek":"175",
        "inst_sync":"176",
        "brand":"177",
        "kaio":"178",
        "cpc":"",
        "lgrpsys":"180",
        "meminfosys":"SYS_lgrpsys",
        "rusagesys":"181",
        "port":"182",
        "pollsys":"183",
        "labelsys":"184",
        "acl":"",
        "auditsys":"186",
        "processor_bind":"187",
        "processor_info":"188",
        "p_online":"189",
        "sigqueue":"190",
        "clock_gettime":"191",
        "clock_settime":"192",
        "clock_getres":"193",
        "timer_create":"194",
        "timer_delete":"195",
        "timer_settime":"196",
        "timer_gettime":"197",
        "timer_getoverrun":"198",
        "nanosleep":"199",
        "facl":"200",
        "door":"201",
        "setreuid":"202",
        "setregid":"203",
        "install_utrap":"204",
        "signotify":"205",
        "schedctl":"206",
        "pset":"207",
        "sparc_utrap_install":"208",
        "resolvepath":"209",
        "lwp_mutex_timedlock":"210",
        "lwp_sema_timedwait":"211",
        "lwp_rwlock_sys":"212",
        "getdents64":"213",
        "mmap64":"214",
        "stat64":"215",
        "lstat64":"216",
        "fstat64":"217",
        "statvfs64":"218",
        "fstatvfs64":"219",
        "setrlimit64":"220",
        "getrlimit64":"221",
        "pread64":"222",
        "pwrite64":"223",
        "creat64":"224",
        "open64":"225",
        "rpcsys":"226",
        "zone":"227",
        "autofssys":"228",
        "getcwd":"229",
        "so_socket":"230",
        "so_socketpair":"231",
        "bind":"232",
        "listen":"233",
        "accept":"234",
        "connect":"235",
        "shutdown":"236",
        "recv":"237",
        "recvfrom":"238",
        "recvmsg":"239",
        "send":"240",
        "sendmsg":"241",
        "sendto":"242",
        "getpeername":"243",
        "getsockname":"244",
        "getsockopt":"245",
        "setsockopt":"246",
        "sockconfig":"247",
        "ntp_gettime":"248",
        "ntp_adjtime":"249",
        "lwp_mutex_unlock":"250",
        "lwp_mutex_trylock":"251",
        "lwp_mutex_register":"252",
        "cladm":"253",
        "uucopy":"254",
        "umount2":"255"

    }

    if key is not None:
        return hex(int(list[sys])).replace("0x", "")
    for key, value in list.items():
        if value == sys:
            return key

def SolarisInterrupted():
    return "91"

#print SolarisSystemcall( "execve", True)

