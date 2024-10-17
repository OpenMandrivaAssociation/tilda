%define name    tilda
%define version 0.9.6
%define release 8

Summary:        Drop Down Terminal for Linux
Name:           %{name}
Version:        %{version}
Release:        %{release}
License:        GPLv2+
Group:          Terminals
Url:            https://tilda.sourceforge.net/
Source:         http://ovh.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
Patch0:		tilda-0.9.6-read-glade.patch
Patch1:		tilda-0.9.6-fix-segfault.patch
Patch3:		tilda-0.9.6-glib.patch


BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(vte)
BuildRequires:  pkgconfig(libconfuse)
BuildRequires:  flex
BuildRequires:  pkgconfig(libglade-2.0)

Requires:       vte
Requires: desktop-file-utils


%description
Linux terminal taking after the likeness
of many classic terminals from first person shooter
games, Quake, Doom and Half-Life to name a few,
where the terminal has no border and is hidden from
the desktop till a key or keys is hit.


%prep
%setup -q -n %{name}-%version
%patch0 -p0
%patch1 -p1
%patch3 -p0

%build
%configure2_5x --disable-rpath
%make

%install
%makeinstall_std

mkdir -p %{buildroot}%{_datadir}/%{name}
mv %{name}.glade %{buildroot}%{_datadir}/%{name}
rm -f %{buildroot}%{_datadir}/%{name}.glade

%find_lang %{name}


%files -f %{name}.lang
%doc ChangeLog COPYING NEWS README
%{_bindir}/tilda
%{_datadir}/applications/tilda.desktop
%{_datadir}/pixmaps/tilda.png
%{_datadir}/%{name}/*.glade


