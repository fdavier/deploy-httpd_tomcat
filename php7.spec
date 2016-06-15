Name:           php
Version:        7.0.7
Release:        1
Summary:        PHP is a widely-used general-purpose scripting language.

Group:          Development/Languages
License:        PHP License v3.01
URL:            http://www.php.net
Source0:        /home/builder/rpmbuild/SOURCES/%{name}-%{version}.tar.gz
BuildRoot:      /home/builder/rpmbuild/TMP/%{name}-%{version}-%{release}-buildroot
BuildRequires: httpd-devel

%description
PHP is a widely-used general-purpose scripting language that is especially
suited for Web development and can be embedded into HTML.

%prep
%setup -q

%build
EXTENSION_DIR=%{_libdir}/php/modules; export EXTENSION_DIR
%configure --with-apxs2=/usr/bin/apxs

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_initrddir}
mkdir -p /home/builder/rpmbuild/BUILDROOT/php-7.0.7-1.x86_64/etc/httpd/conf/
cp /etc/httpd/conf/httpd.conf /home/builder/rpmbuild/BUILDROOT/php-7.0.7-1.x86_64/etc/httpd/conf/
%{__make} install INSTALL_ROOT="%{buildroot}"

# Grep reports BUILDROOT inside our object files; disable that test.
QA_SKIP_BUILD_ROOT=1
export QA_SKIP_BUILD_ROOT

%clean
rm -rf %{buildroot}

%files
/.channels/.alias/pear.txt
/.channels/.alias/pecl.txt
/.channels/.alias/phpdocs.txt
/.channels/__uri.reg
/.channels/doc.php.net.reg
/.channels/pear.php.net.reg
/.channels/pecl.php.net.reg
/.depdb
/.depdblock
/.filemap
/.lock
%{_bindir}/pear
%{_bindir}/peardev
%{_bindir}/pecl
%{_bindir}/phar
%{_bindir}/phar.phar
%{_bindir}/php
%{_bindir}/php-cgi
%{_bindir}/php-config
%{_bindir}/phpdbg
%{_bindir}/phpize
%{_sysconfdir}/pear.conf
%{_sysconfdir}/httpd/conf/
%{_libdir}/build/
%{_libdir}/php/
%{_libdir}/httpd/
%{_prefix}/include/php/
%{_mandir}/man1/
