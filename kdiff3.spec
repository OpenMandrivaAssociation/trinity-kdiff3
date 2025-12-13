%bcond clang 1

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 2

%define tde_pkg kdiff3
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	0.9.91
Release:	%{?tde_version}_%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Summary:	KDiff3 is a utility for comparing and/or merging two or three text files or directories.
Group:		Applications/Utilities
URL:		http://www.trinitydesktop.org/

License:	GPLv2+

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}

Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/development/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

BuildSystem:    cmake
BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_SKIP_RPATH=OFF
BuildOption:    -DCMAKE_SKIP_INSTALL_RPATH=OFF
BuildOption:    -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON
BuildOption:    -DCMAKE_INSTALL_RPATH="%{tde_libdir}"
BuildOption:    -DCMAKE_INSTALL_PREFIX="%{tde_prefix}"
BuildOption:    -DSHARE_INSTALL_PREFIX="%{tde_datadir}"
BuildOption:    -DLIB_INSTALL_DIR="%{tde_libdir}"
BuildOption:    -DPLUGIN_INSTALL_DIR="%{tde_tdelibdir}"
BuildOption:    -DWITH_ALL_OPTIONS=ON -DBUILD_ALL=ON -DBUILD_DOC=ON
BuildOption:    -DBUILD_TRANSLATIONS=ON

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	libtool

# ACL support
BuildRequires:  pkgconfig(libacl)

# IDN support
BuildRequires:	pkgconfig(libidn)

# OPENSSL support
BuildRequires:  pkgconfig(openssl)

BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)


%description
Shows the differences line by line and character by character (!).
Provides an automatic merge-facility and
an integrated editor for comfortable solving of merge-conflicts.
Supports TDEIO on TDE (allows accessing ftp, sftp, fish, smb etc.).
Unicode & UTF-8 support


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"


%install -a
# Unwanted files
# These are not HTML files but weird files in wrong place ??
%__rm -rf %{?buildroot}%{tde_tdedocdir}/HTML/kdiff3/

%find_lang %{tde_pkg}
%find_lang %{tde_pkg}_plugin
cat "%{tde_pkg}_plugin.lang" >>"%{tde_pkg}.lang"


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{tde_bindir}/kdiff3
%{tde_datadir}/apps/kdiff3/
%{tde_datadir}/apps/kdiff3part/
%{tde_datadir}/icons/hicolor/*/apps/kdiff3.png
%{tde_datadir}/icons/locolor/*/apps/kdiff3.png
%{tde_docdir}/kdiff3/
%{tde_tdedocdir}/HTML/*/kdiff3/
%{tde_datadir}/services/kdiff3_plugin.desktop
%{tde_datadir}/services/kdiff3part.desktop
%{tde_tdeappdir}/kdiff3.desktop
%{tde_datadir}/applnk/.hidden/kdiff3plugin.desktop
%{tde_mandir}/man*/*
%{tde_tdelibdir}/libkdiff3part.la
%{tde_tdelibdir}/libkdiff3part.so
%{tde_tdelibdir}/libkdiff3plugin.la
%{tde_tdelibdir}/libkdiff3plugin.so

