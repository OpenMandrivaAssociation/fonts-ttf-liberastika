%define pkgname liberastika-ttf

Summary: Sans fonts derived from Liberation Sans
Name: fonts-ttf-liberastika
Version: 1.1.3
Release: 2
License: GPLv2 with exception
Group: System/Fonts/True type
URL: http://code.google.com/p/liberastika/
Source0: http://liberastika.googlecode.com/files/%{pkgname}-%{version}.tar.xz
BuildArch: noarch
BuildRequires: freetype-tools

%description
The font based on Liberation Sans with some cyrillic letters modified. It is
metrically incompatible with Arial fonts.

%prep
%setup -q -c -n %{pkgname}-%{version}

%build

%install
%__mkdir_p %{buildroot}%{_xfontdir}/TTF/liberastika

%__install -m 644 *.ttf %{buildroot}%{_xfontdir}/TTF/liberastika
ttmkfdir %{buildroot}%{_xfontdir}/TTF/liberastika > %{buildroot}%{_xfontdir}/TTF/liberastika/fonts.dir
%__ln_s fonts.dir %{buildroot}%{_xfontdir}/TTF/liberastika/fonts.scale

%__mkdir_p %{buildroot}%_sysconfdir/X11/fontpath.d/
%__ln_s ../../..%{_xfontdir}/TTF/liberastika \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-liberastika:pri=50

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README ChangeLog
%dir %{_xfontdir}/TTF/liberastika
%{_xfontdir}/TTF/liberastika/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/liberastika/fonts.dir
%{_xfontdir}/TTF/liberastika/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-liberastika:pri=50





%changelog
* Fri Jul 22 2011 Sergey Zhemoitel <serg@mandriva.org> 1.1.3-1mdv2012.0
+ Revision: 690986
- imported package fonts-ttf-liberastika

