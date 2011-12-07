Summary: QPid QMF interface to Libvirt
Name: libvirt-qpid
Version: 0.2.22
Release: 3%{?dist}
Source: libvirt-qpid-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
License: LGPLv2+
ExclusiveArch: i686 x86_64
Group: Applications/System
Requires: libxml2 >= 2.7.1
Requires: qmf >= 0.5.790661
Requires: qpid-cpp-client >= 0.5.790661
Requires: libvirt >= 0.4.4
Requires(post):  /sbin/chkconfig
Requires(preun): /sbin/chkconfig
Requires(preun): initscripts
BuildRequires: qpid-cpp-client-devel >= 0.5.790661
BuildRequires: libxml2-devel >= 2.7.1
BuildRequires: libvirt-devel >= 0.5.0
BuildRequires: qmf-devel >= 0.5.790661
Url: http://libvirt.org/qpid

%description

libvirt-qpid provides an interface with libvirt using QMF (qpid modeling
framework) which utilizes the AMQP protocol.  The Advanced Message Queuing
Protocol (AMQP) is an open standard application layer protocol providing
reliable transport of messages.

QMF provides a modeling framework layer on top of qpid (which implements 
AMQP).  This interface allows you to manage hosts, domains, pools etc. as
a set of objects with properties and methods.

%prep
%setup -q

%build
%configure
make

%install
rm -rf %{buildroot}
%makeinstall

%post
/sbin/chkconfig --add libvirt-qpid --level -
/sbin/service libvirt-qpid condrestart

%preun
if [ $1 = 0 ]; then
    /sbin/service libvirt-qpid stop >/dev/null 2>&1 || :
    chkconfig --del libvirt-qpid
fi

%postun
if [ "$1" -ge "1" ]; then
    /sbin/service libvirt-qpid condrestart >/dev/null 2>&1 || :
fi

%clean
test "x$RPM_BUILD_ROOT" != "x" && rm -rf $RPM_BUILD_ROOT

%files

%defattr(644, root, root, 755)
%dir %{_datadir}/libvirt-qpid/
%{_datadir}/libvirt-qpid/libvirt-schema.xml

%attr(755, root, root) %{_sbindir}/libvirt-qpid
%attr(755, root, root) %{_sysconfdir}/rc.d/init.d/libvirt-qpid
%config(noreplace) %{_sysconfdir}/sysconfig/libvirt-qpid

%doc AUTHORS COPYING


%changelog
* Wed Jul 28 2010 Ian Main <imain@redhat.com> 0.2.22-3
- Rebuild against new qpid/qmf.  Resolves: #618876

* Mon Jul 19 2010 Ian Main <imain@redhat.com> 0.2.22-2
- Rebuild against new qpid/qmf.  Resolves: #614750

* Tue Jul  6 2010 Ian Main <imain@redhat.com> 0.2.22-1
- Fix init script to return 2 when invoked with no arguments and add try-restart
  to usage list.  Resolves: #570492

* Mon Jun 28 2010 Ian Main <imain@redhat.com> 0.2.21-3
- Somehow I didn't get the right upstream sources for the index keyword bug.
  Resolves: #596682

* Sat Jun 19 2010 Alan Pevec <apevec@redhat.com> 0.2.21-2
- rebuild for new qpid-cpp, see #604173

* Tue May 25 2010 Ian Main <imain@redhat.com> - 0.2.21-1
- Misunderstanding of the 'index' keyword was making all objects have the same 
  id. Resolves: #596682

* Tue May 25 2010 Ian Main <imain@redhat.com> - 0.2.20-2
- Fix spurrious declaration. Resolves: #592851

* Tue May 25 2010 Ian Main <imain@redhat.com> - 0.2.20-1
- Fix header in PoolWrap.cpp. Resolves: #592851

* Tue May 25 2010 Ian Main <imain@redhat.com> - 0.2.19-1
- Updates to work with API changes in new qpid release, move to upstream codebase. 
  Resolves: #592851

* Wed May 19 2010 Ian Main <imain@redhat.com> - 0.2.17-9
- Another rebuild against new qpid packages.  Resolves: #592851

* Wed May 19 2010 Ian Main <imain@redhat.com> - 0.2.17-8
- Rebuild against new qpid packages.  Resolves: #592851

* Tue Feb 2 2010 Ian Main <imain@redhat.com> - 0.2.17-7
- Add ExclusiveArch to match qpid builds.  Resolves: #560015

* Tue Feb 2 2010 Ian Main <imain@redhat.com> - 0.2.17-6
- Finally got the package names right.  Resolves: #560015

* Mon Feb 1 2010 Ian Main <imain@redhat.com> - 0.2.17-5
- Use qpid-devel instead of qpid-cpp-devel.  Resolves: #560015

* Mon Feb 1 2010 Ian Main <imain@redhat.com> - 0.2.17-4
- s/qpidc/qpid-cpp/ for qpid package name change.  Resolves: #560015

* Thu Dec 10 2009 Ian Main <imain@redhat.com> - 0.2.17-3
- Woops, don't need -lqmfengine.

* Thu Nov 05 2009 Ian Main <imain@redhat.com> - 0.2.17-2
- Fix libraries for new qpidc in src.

* Fri Oct 02 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.2.17-1
- Rebuild for new qpidc.

* Mon Jul 27 2009 Arjun Roy <arroy@redhat.com> - 0.2.17.0
- Fixed a bug related to updating of cached pool sources.

* Fri Jun 05 2009 Ian Main <imain@redhat.com> - 0.2.16-5
- Bump for new build.

* Fri Jun 05 2009 Ian Main <imain@redhat.com> - 0.2.16-2
- Spec fixes.

* Fri Jun 05 2009 Ian Main <imain@redhat.com> - 0.2.16-1
- Cache calls to get storage XML as they take a LONG time.  This
  greatly speeds up volume enumeration.

* Thu May 28 2009 Ian Main <imain@redhat.com> - 0.2.16-1
- Cache calls to get storage XML as they take a LONG time.  This
  greatly speeds up volume enumeration.

* Thu May 28 2009 Ian Main <imain@redhat.com> - 0.2.15-1
- Fix migration bug.

* Thu May 07 2009 Ian Main <imain@redhat.com> - 0.2.14-4
- Bump release for F11.

* Thu May 07 2009 Ian Main <imain@redhat.com> - 0.2.14-3
- Update requires for latest version of qpid.

* Thu May 07 2009 Ian Main <imain@redhat.com> - 0.2.14-2
- Rebuild for new qpid.

* Thu May 07 2009 Ian Main <imain@redhat.com> - 0.2.14-1
- Rebuild for new qpid.

* Thu Mar 26 2009 Ian Main <imain@redhat.com> - 0.2.14-0
- Added refresh method to storage pools.

* Thu Mar 26 2009 Ian Main <imain@redhat.com> - 0.2.13-1
- Add throws to constructors in case one of the libvirt calls
  fails.  Pretty sure this was the cause of some segfaults.

* Thu Mar 26 2009 Ian Main <imain@redhat.com> - 0.2.12-3
- Added dist to release version.

* Wed Feb 25 2009 Ian Main <imain@redhat.com> - 0.2.12-2
- Fixed permissions in specfile.

* Wed Feb 25 2009 Ian Main <imain@redhat.com> - 0.2.12-1
- Fixed various specfile issues.

* Tue Feb 03 2009 Ian Main <imain@redhat.com> - 0.2.12-0
- Added parentVolume to support LVM parent recognition.

* Fri Jan 23 2009 Ian Main <imain@redhat.com> - 0.2.10-0
- Added support for gssapi.

* Fri Dec 12 2008 Ian Main <imain@redhat.com> - 0.2.4-0
- Added 'findStoragePoolSources' method.

* Thu Dec 4 2008 Ian Main <imain@redhat.com> - 0.2.3-0
- Added 'build' method to storage pool.
- Build against newer libvirt and qpid.

* Wed Nov 20 2008 Ian Main <imain@redhat.com> - 0.2.2-0
- Change update interval to 3 seconds, update version.

* Wed Nov 19 2008 Ian Main <imain@redhat.com> - 0.2.2-0
- Rebase to newer qpid.

* Thu Oct 30 2008 Ian Main <imain@redhat.com> - 0.2.1-0
- Use lstr for xml descriptions.  This lets you have greater than
  255 characters in the string.
- Fix bug in calling of getXMLDesc.

* Wed Oct 15 2008 Ian Main <imain@redhat.com> - 0.2.0-0
- API changed to camel case.
- Return libvirt error codes.
- Reconnect on libvirt disconnect.
- Implement node info.
- New release.

* Wed Oct 1 2008 Ian Main <imain@redhat.com> - 0.1.3-0
- Bugfixes, memory leaks fixed etc.

* Tue Sep 30 2008 Ian Main <imain@redhat.com> - 0.1.2-0
- Updated spec to remove qpidd requirement.
- Added libvirt-qpid sysconfig file.

* Fri Sep 26 2008 Ian Main <imain@redhat.com> - 0.1.2-0
- Setup daemonization and init scripts.
- Added getopt for command line parsing.

* Fri Sep 19 2008 Ian Main <imain@redhat.com> - 0.1.1-0
- Initial packaging.



