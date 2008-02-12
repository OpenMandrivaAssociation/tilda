%define name    tilda
%define version 0.9.5
%define release %mkrel 1

Summary:        Tilda - Drop Down Terminal for Linux
Name:           %{name}
Version:        %{version}
Release:        %{release}
License:        GPLv2+
Group:          Terminals
Url:            http://tilda.sourceforge.net/
Source:         http://ovh.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot

BuildRequires:  pkgconfig
BuildRequires:  vte-devel
BuildRequires:  confuse-devel
BuildRequires:  flex
BuildRequires:  libglade2.0-devel

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

mkdir -p %{buildroot}%{_datadir}/%{name}
mv %{name}.glade %{buildroot}%{_datadir}/%{name}
rm -f %{buildroot}%{_datadir}/%{name}.glade

%find_lang %{name}

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/tilda
%{_datadir}/applications/tilda.desktop
%{_datadir}/pixmaps/tilda.png
%{_datadir}/%{name}/*.glade
