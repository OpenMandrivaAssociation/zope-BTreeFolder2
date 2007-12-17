%define product		BTreeFolder2
%define version		1.0.2
%define release		2

%define zope_minver	2.7

%define zope_home	%{_prefix}/lib/zope
%define software_home	%{zope_home}/lib/python

Summary:	BTreeFolder2 is a Zope product that acts like a Zope folder but can store many more items
Name:		zope-%{product}
Version:	%{version}
Release:	%mkrel %{release}
License:	ZPL
Group:		System/Servers
Source:		http://plone.org/Members/tiran/BTreeFolder2-1.0.2.tar.bz2
URL:		http://hathawaymix.org/Software/BTreeFolder2
BuildArch:	noarch
Requires:	zope >= %{zope_minver}

Provides:	BTreeFolder2 = %{version}-%{release}
Obsoletes:	BTreeFolder2

%description
When you fill a Zope folder with too many items, both Zope and your browser get
overwhelmed. Zope has to load and store a large folder object, and the browser
has to render large HTML tables repeatedly. Zope can store a lot of objects, but
it has trouble storing a lot of objects in a single standard folder.

BTreeFolder2 solves this problem by storing subobjects in Zope BTrees, special
structures designed for an object database. BTrees can hold numerous items
without loading them all into memory at once.

This product descends from the BTreeFolder product. Since they are more
optimized, BTreeFolder2 instances can hold more objects than BTreeFolder
instances. But since there are products that depend on the internal structure of
BTreeFolder, the product has been renamed to make it possible to have both
installed at the same time. New software should depend on BTreeFolder2, not
BTreeFolder.

This product also includes CMFBTreeFolder, which will be made available if you
also have CMF installed.

%prep
%setup -c

%build
# Not much, eh? :-)


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__cp} -a * %{buildroot}%{software_home}/Products/


%clean
%{__rm} -rf %{buildroot}

%post
if [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
	service zope restart
fi

%postun
if [ -f "%{_prefix}/bin/zopectl" ] && [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
	service zope restart
fi

%files
%defattr(0644, root, root, 0755)
%{software_home}/Products/*


