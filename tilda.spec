%define name    tilda
%define version 0.9.4
%define release %mkrel 1

%define section System/Terminals
%define title   Tilda
%define longtitle Tilda - Drop Down Terminal for Linux


Summary:        %{longtitle}
Name:           %{name}
Version:        %{version}
Release:        %{release}
License:        GPL
Group:          Terminals
Url:            http://tilda.sourceforge.net/ 
Source:         http://ovh.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot

BuildRequires:  pkgconfig
BuildRequires:  vte-devel
BuildRequires:  confuse-devel

Requires:       vte
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description

Tilda is a Linux terminal taking after the likeness 
of many classic terminals from first person shooter
games, Quake, Doom and Half-Life to name a few,
where the terminal has no border and is hidden from 
the desktop till a key or keys is hit.


%prep
%setup -q -n %{name}-%version

%build


%configure2_5x --disable-rpath

%make



%install
rm -rf $RPM_BUILD_ROOT


%makeinstall

%find_lang %{name}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name="%{title}"
Comment="%{summary}"
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=TerminalEmulator;X-MandrivaLinux-System-Terminals;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/tilda
%{_datadir}/applications/mandriva-tilda.desktop
%exclude %{_datadir}/applications/tilda.desktop
%{_datadir}/pixmaps/tilda.png


