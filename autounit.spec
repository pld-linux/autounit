Summary:	GNU Autounit - unit testing frameworks for Autoconf
Summary(pl):	GNU Autoconf - szkielet do testów dla Autoconfa
Name:		autounit
Version:	0.10.2
Release:	2
License:	GPL
Group:		Development/Tools
Source0:	http://www.recursism.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	85ba614a10c789644a7ee986c496dcb3
Patch0:		%{name}-info.patch
Patch1:		%{name}-no_html_doc.patch
URL:		http://www.recursism.com/web/index.php?action=page&name=autounit
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Autounit's goal is to provide a common unit testing framework for
application developers who use GNU Autoconf already in their projects
but do not currently use a unit testing framework.

%description -l pl
Celem programu GNU Autounit jest dostarczenie wspólnego systemu testów
dla twórców aplikacji ju¿ u¿ywaj±cych programu GNU Autoconf w swoich
projektach, ale aktualnie nie u¿ywaj±cych programów testuj±cych.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__libtoolize}
%{__autoheader}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/libau-c-unit.a
%{_includedir}/c-unit
%{_infodir}/*info*
