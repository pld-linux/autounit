Summary:	GNU Autounit - unit testing frameworks for Autoconf
Summary(pl):	GNU Autoconf - szkielet do testów dla Autoconfa
Name:		autounit
Version:	0.15.2
Release:	2
License:	GPL
Group:		Development/Tools
Source0:	http://www.recursism.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	ce0469ca0a9e421670918fcaf52fd8b6
Patch0:		%{name}-info.patch
Patch1:		%{name}-no_html_doc.patch
Patch2:		%{name}-Makefile.patch
URL:		http://www.recursism.com/web/index.php?action=page&name=autounit
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib-devel
BuildRequires:	libtool
Requires(post,preun):	/sbin/ldconfig
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
%patch2 -p1

%build
cp -f /usr/share/automake/config.sub .
%{__gettextize}
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
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libau-c-unit.so.*.*.*
%attr(755,root,root) %{_libdir}/libau-c-unit.so
%{_libdir}/libau-c-unit.la
%{_libdir}/libau-c-unit.a
%{_includedir}/autounit
%{_datadir}/guile/autounit
%{_pkgconfigdir}/*.pc
%{_aclocaldir}/*.m4
%{_infodir}/autounit.info*
