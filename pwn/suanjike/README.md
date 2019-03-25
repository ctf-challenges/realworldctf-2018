Building sandbox for evaluating untrusted codes is hard. Why not simply use Docker? Looks like they have [put][1] [a lot of][2] [effort][3] [into][4] [security][5]. With a modern enough distribution like Ubuntu Server 18.04 it must be very safe even without upgrading.

Check the attachments for how exactly servers were built: [build.sh][6]

Note: No 0 day involved. No kernel bugs involved.

Hint: usermode helper is always executed in the initial namespace, and the intended bug is almost certainly Ubuntu specific.

[1]: https://github.com/moby/moby/blob/master/profiles/apparmor/template.go
[2]: https://docs.docker.com/engine/security/non-events/
[3]: https://www.mankier.com/8/docker_selinux
[4]: https://github.com/moby/moby/blob/master/profiles/seccomp/default.json
[5]: https://docs.docker.com/engine/security/security/
[6]: https://drive.google.com/file/d/1eIoqgM3kjNL7sF5QOjY1_3FmHv06xwaJ/view?usp=sharing