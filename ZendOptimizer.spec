%define _srcname ZendOptimizer-Beta4-Linux-glibc2.1
Summary:	Zend Optimizer - php4 code optimizer
Summary(pl):	Zend Optimizer - optymalizator kodu php4
Name:		ZendOptimizer
Version:	0.98beta4
Release:	1
License:	Trial, not distributable
Group:		Libraries
Source0:	%{_srcname}.tar.gz
NoSource:	0
URL:		http://www.zend.com/zend/optimizer.php
Requires:	php >= 4.0.0
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Zend Optimizer - php4 code optimizer.

%description -l pl
Zend Optimizer - optymalizator kodu php4.

%prep
%setup -q -n %{_srcname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/apache/php

install ZendOptimizer.so $RPM_BUILD_ROOT%{_libdir}/apache/php

%clean
rm -rf $RPM_BUILD_ROOT

%preun
if [ -f /etc/php/php.ini ]; then
        echo "deactivating module 'ZendOptimizer.so' in php.ini" 1>&2
   perl -pi -e 's|^zend_optimizer.optimization_level|;zend_optimizer.optimization_level|g' \
   /etc/php/php.ini
   perl -pi -e 's|^zend_extension=/usr/lib/apache/php/ZendOptimizer.so"|;zend_extension="/usr/lib/apache/php/ZendOptimizer.so"|g' \
   /etc/php/php.ini

fi

%post
if [ -f /etc/php/php.ini ]; then
        echo "activating module 'ZendOptimizer.so' in php.ini" 1>&2
   perl -pi -e 's|^;zend_optimizer.optimization_level|zend_optimizer.optimization_level|g' \
   /etc/php/php.ini
   perl -pi -e 's|^;zend_extension="/usr/lib/apache/php/ZendOptimizer.so"|zend_extension="/usr/lib/apache/php/ZendOptimizer.so"|g' \
   /etc/php/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
        /etc/rc.d/init.d/httpd restart 1>&2
fi
echo "Remember:Read the /usr/share/doc/ZendOptimizer-%{version}/LICENSE.gz!"

%files
%defattr(644,root,root,755)
%doc FAQ.txt LICENSE acceleratedbyoptimizer.gif
%attr(755,root,root) %{_libdir}/apache/php/ZendOptimizer.so
