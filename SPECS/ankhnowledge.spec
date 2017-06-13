Name: Ankhnowledge
Version: 0.5.2
Release:        1%{?dist}
Summary: Turn-Based Game Developt at UnB in the Ancient Egypt

License: GPL2
URL: https://github.com/sconetto/Ankhnowledge
Source0: https://github.com/sconetto/Ankhnowledge/archive/ankhnowledge-0.5.2.tar.gz

BuildRequires: gcc,make,gcc-c++,autoconf,automake,libstdc++-devel,libstdc++,SDL_image,SDL_image-devel,SDL_ttf,SDL_ttf-devel,SDL_mixer,SDL_mixer-devel,SDL_net,SDL_net-devel

%description
Ankhnowledge is a multiplayer game made in C ++ with the help of the free
multimedia library SDL (Simple DirectMedia Layer) that was produced during
the course of Introduction to Electronic Games (IJE) at UnB - Universidade
de Brasília Campus Gama.
The game is in the ancient Egypt, where two players vie to see who is
the best explorer.


%prep
%autosetup
/bin/bash %_builddir/Ankhnowledge-0.5.2/cleanup.sh
/bin/bash %_builddir/Ankhnowledge-0.5.2/bootstrap.sh

%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%license COPYING
%doc README.md


%changelog
* Tue Jun 13 2017 João Pedro Sconetto
- Initial Release of Ankhnowledge
