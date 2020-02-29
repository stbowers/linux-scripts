cat | jgmenu --simple <<'EOT'
Lock,dm-tool lock,system-lock-screen
Log Out,i3 exit,system-log-out
^sep()
Sleep,systemctl suspend,system-suspend
Hibernate,systemctl hibernate,system-suspend-hibernate
Shutdown,systemctl shutdown,system-shutdown
Reboot,systemctl reboot,system-reboot
EOT
