%bcond clang 1

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 2

%define tde_pkg kdiff3
%define tde_prefix /opt/trinity


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


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/development/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DPLUGIN_INSTALL_DIR=%{tde_prefix}/%{_lib}/trinity
BuildOption:    -DWITH_ALL_OPTIONS=ON -DBUILD_ALL=ON -DBUILD_DOC=ON
BuildOption:    -DBUILD_TRANSLATIONS=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

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
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig"


%install -a
# Unwanted files
# These are not HTML files but weird files in wrong place ??
%__rm -rf %{?buildroot}%{tde_prefix}/share/doc/tde/HTML/kdiff3/

%find_lang %{tde_pkg}
%find_lang %{tde_pkg}_plugin
cat "%{tde_pkg}_plugin.lang" >>"%{tde_pkg}.lang"


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{tde_prefix}/bin/kdiff3
%{tde_prefix}/share/apps/kdiff3/
%{tde_prefix}/share/apps/kdiff3part/
%{tde_prefix}/share/icons/hicolor/*/apps/kdiff3.png
%{tde_prefix}/share/icons/locolor/*/apps/kdiff3.png
%{tde_prefix}/share/doc/kdiff3/
%{tde_prefix}/share/doc/tde/HTML/*/kdiff3/
%{tde_prefix}/share/services/kdiff3_plugin.desktop
%{tde_prefix}/share/services/kdiff3part.desktop
%{tde_prefix}/share/applications/tde/kdiff3.desktop
%{tde_prefix}/share/applnk/.hidden/kdiff3plugin.desktop
%{tde_prefix}/share/man/man*/*
%{tde_prefix}/%{_lib}/trinity/libkdiff3part.la
%{tde_prefix}/%{_lib}/trinity/libkdiff3part.so
%{tde_prefix}/%{_lib}/trinity/libkdiff3plugin.la
%{tde_prefix}/%{_lib}/trinity/libkdiff3plugin.so

