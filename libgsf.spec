#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libgsf
Version  : 1.14.49
Release  : 6
URL      : https://download.gnome.org/sources/libgsf/1.14/libgsf-1.14.49.tar.xz
Source0  : https://download.gnome.org/sources/libgsf/1.14/libgsf-1.14.49.tar.xz
Summary  : GNOME Structured File library
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: libgsf-bin = %{version}-%{release}
Requires: libgsf-data = %{version}-%{release}
Requires: libgsf-lib = %{version}-%{release}
Requires: libgsf-license = %{version}-%{release}
Requires: libgsf-locales = %{version}-%{release}
Requires: libgsf-man = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(gobject-introspection-1.0)

%description
A library for reading and writing structured files (eg MS OLE and Zip)

%package bin
Summary: bin components for the libgsf package.
Group: Binaries
Requires: libgsf-data = %{version}-%{release}
Requires: libgsf-license = %{version}-%{release}

%description bin
bin components for the libgsf package.


%package data
Summary: data components for the libgsf package.
Group: Data

%description data
data components for the libgsf package.


%package dev
Summary: dev components for the libgsf package.
Group: Development
Requires: libgsf-lib = %{version}-%{release}
Requires: libgsf-bin = %{version}-%{release}
Requires: libgsf-data = %{version}-%{release}
Provides: libgsf-devel = %{version}-%{release}
Requires: libgsf = %{version}-%{release}

%description dev
dev components for the libgsf package.


%package doc
Summary: doc components for the libgsf package.
Group: Documentation
Requires: libgsf-man = %{version}-%{release}

%description doc
doc components for the libgsf package.


%package lib
Summary: lib components for the libgsf package.
Group: Libraries
Requires: libgsf-data = %{version}-%{release}
Requires: libgsf-license = %{version}-%{release}

%description lib
lib components for the libgsf package.


%package license
Summary: license components for the libgsf package.
Group: Default

%description license
license components for the libgsf package.


%package locales
Summary: locales components for the libgsf package.
Group: Default

%description locales
locales components for the libgsf package.


%package man
Summary: man components for the libgsf package.
Group: Default

%description man
man components for the libgsf package.


%prep
%setup -q -n libgsf-1.14.49
cd %{_builddir}/libgsf-1.14.49

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1647873850
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1647873850
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libgsf
cp %{_builddir}/libgsf-1.14.49/COPYING %{buildroot}/usr/share/package-licenses/libgsf/217bce14cea37348f2a0182adf35c02137ed9a01
cp %{_builddir}/libgsf-1.14.49/COPYING.LIB %{buildroot}/usr/share/package-licenses/libgsf/9a8724b113a48b8654879231e204c01029e94f92
%make_install
%find_lang libgsf

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gsf
/usr/bin/gsf-office-thumbnailer
/usr/bin/gsf-vba-dump

%files data
%defattr(-,root,root,-)
/usr/share/thumbnailers/gsf-office.thumbnailer

%files dev
%defattr(-,root,root,-)
/usr/include/libgsf-1/gsf/gsf-blob.h
/usr/include/libgsf-1/gsf/gsf-clip-data.h
/usr/include/libgsf-1/gsf/gsf-doc-meta-data.h
/usr/include/libgsf-1/gsf/gsf-docprop-vector.h
/usr/include/libgsf-1/gsf/gsf-fwd.h
/usr/include/libgsf-1/gsf/gsf-impl-utils.h
/usr/include/libgsf-1/gsf/gsf-infile-impl.h
/usr/include/libgsf-1/gsf/gsf-infile-msole.h
/usr/include/libgsf-1/gsf/gsf-infile-msvba.h
/usr/include/libgsf-1/gsf/gsf-infile-stdio.h
/usr/include/libgsf-1/gsf/gsf-infile-tar.h
/usr/include/libgsf-1/gsf/gsf-infile-zip.h
/usr/include/libgsf-1/gsf/gsf-infile.h
/usr/include/libgsf-1/gsf/gsf-input-bzip.h
/usr/include/libgsf-1/gsf/gsf-input-gio.h
/usr/include/libgsf-1/gsf/gsf-input-gzip.h
/usr/include/libgsf-1/gsf/gsf-input-http.h
/usr/include/libgsf-1/gsf/gsf-input-impl.h
/usr/include/libgsf-1/gsf/gsf-input-iochannel.h
/usr/include/libgsf-1/gsf/gsf-input-memory.h
/usr/include/libgsf-1/gsf/gsf-input-proxy.h
/usr/include/libgsf-1/gsf/gsf-input-stdio.h
/usr/include/libgsf-1/gsf/gsf-input-textline.h
/usr/include/libgsf-1/gsf/gsf-input.h
/usr/include/libgsf-1/gsf/gsf-libxml.h
/usr/include/libgsf-1/gsf/gsf-meta-names.h
/usr/include/libgsf-1/gsf/gsf-msole-utils.h
/usr/include/libgsf-1/gsf/gsf-open-pkg-utils.h
/usr/include/libgsf-1/gsf/gsf-opendoc-utils.h
/usr/include/libgsf-1/gsf/gsf-outfile-impl.h
/usr/include/libgsf-1/gsf/gsf-outfile-msole.h
/usr/include/libgsf-1/gsf/gsf-outfile-stdio.h
/usr/include/libgsf-1/gsf/gsf-outfile-zip.h
/usr/include/libgsf-1/gsf/gsf-outfile.h
/usr/include/libgsf-1/gsf/gsf-output-bzip.h
/usr/include/libgsf-1/gsf/gsf-output-csv.h
/usr/include/libgsf-1/gsf/gsf-output-gio.h
/usr/include/libgsf-1/gsf/gsf-output-gzip.h
/usr/include/libgsf-1/gsf/gsf-output-iconv.h
/usr/include/libgsf-1/gsf/gsf-output-impl.h
/usr/include/libgsf-1/gsf/gsf-output-iochannel.h
/usr/include/libgsf-1/gsf/gsf-output-memory.h
/usr/include/libgsf-1/gsf/gsf-output-stdio.h
/usr/include/libgsf-1/gsf/gsf-output.h
/usr/include/libgsf-1/gsf/gsf-shared-memory.h
/usr/include/libgsf-1/gsf/gsf-structured-blob.h
/usr/include/libgsf-1/gsf/gsf-timestamp.h
/usr/include/libgsf-1/gsf/gsf-utils.h
/usr/include/libgsf-1/gsf/gsf.h
/usr/lib64/libgsf-1.so
/usr/lib64/pkgconfig/libgsf-1.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/gsf/annotation-glossary.html
/usr/share/gtk-doc/html/gsf/api.html
/usr/share/gtk-doc/html/gsf/dependencies.html
/usr/share/gtk-doc/html/gsf/gsf-Compression.html
/usr/share/gtk-doc/html/gsf/gsf-GIO.html
/usr/share/gtk-doc/html/gsf/gsf-GIOChannel.html
/usr/share/gtk-doc/html/gsf/gsf-Infile-reading-structed-files.html
/usr/share/gtk-doc/html/gsf/gsf-Input-from-unstructured-files.html
/usr/share/gtk-doc/html/gsf/gsf-MS-OLE2.html
/usr/share/gtk-doc/html/gsf/gsf-OASIS-Open-Document.html
/usr/share/gtk-doc/html/gsf/gsf-Outfile-writing-structed-files.html
/usr/share/gtk-doc/html/gsf/gsf-Output-to-unstructured-files.html
/usr/share/gtk-doc/html/gsf/gsf-Reading-and-Writing-from-local-files-and-directories.html
/usr/share/gtk-doc/html/gsf/gsf-Text.html
/usr/share/gtk-doc/html/gsf/gsf-Utilities.html
/usr/share/gtk-doc/html/gsf/gsf-XML-and-libxml.html
/usr/share/gtk-doc/html/gsf/gsf-Zip.html
/usr/share/gtk-doc/html/gsf/gsf-blobs.html
/usr/share/gtk-doc/html/gsf/gsf-clip-data.html
/usr/share/gtk-doc/html/gsf/gsf-index.html
/usr/share/gtk-doc/html/gsf/gsf-memory.html
/usr/share/gtk-doc/html/gsf/gsf-metadata.html
/usr/share/gtk-doc/html/gsf/gsf-users.html
/usr/share/gtk-doc/html/gsf/gsf.devhelp2
/usr/share/gtk-doc/html/gsf/history.html
/usr/share/gtk-doc/html/gsf/home.png
/usr/share/gtk-doc/html/gsf/index.html
/usr/share/gtk-doc/html/gsf/intro.html
/usr/share/gtk-doc/html/gsf/io.html
/usr/share/gtk-doc/html/gsf/left-insensitive.png
/usr/share/gtk-doc/html/gsf/left.png
/usr/share/gtk-doc/html/gsf/misc.html
/usr/share/gtk-doc/html/gsf/parsers.html
/usr/share/gtk-doc/html/gsf/right-insensitive.png
/usr/share/gtk-doc/html/gsf/right.png
/usr/share/gtk-doc/html/gsf/sources.html
/usr/share/gtk-doc/html/gsf/style.css
/usr/share/gtk-doc/html/gsf/up-insensitive.png
/usr/share/gtk-doc/html/gsf/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgsf-1.so.114
/usr/lib64/libgsf-1.so.114.0.49

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libgsf/217bce14cea37348f2a0182adf35c02137ed9a01
/usr/share/package-licenses/libgsf/9a8724b113a48b8654879231e204c01029e94f92

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gsf-office-thumbnailer.1
/usr/share/man/man1/gsf-vba-dump.1
/usr/share/man/man1/gsf.1

%files locales -f libgsf.lang
%defattr(-,root,root,-)

