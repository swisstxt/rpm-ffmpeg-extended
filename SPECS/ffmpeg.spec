%global service_name %{name}

Name:           %{name}
Version:        %{ver}
Release:        %{rel}%{?dist}
Summary:        Hyper fast MPEG1/MPEG4/H263/RV and AC3/MPEG audio encoder for RHEL/CENTOS %{os_rel}
BuildArch:      %{arch}
Group:          System Environment/Libraries
License:        commercial
URL:            http://ffmpeg.sourceforge.net/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  libvpx-devel >= 1.3.0
BuildRequires:  opus-devel
BuildRequires:  libvorbis-devel

Source:         http://ffmpeg.org/releases/%{name}-%{version}.tar.bz2

%description
Hyper fast MPEG1/MPEG4/H263/RV and AC3/MPEG audio encoder for RHEL/CENTOS %{os_rel}

%prep
test -f version.h || echo "#define FFMPEG_VERSION \"%{evr}\"" > version.h

%build

%install

%clean

%files

%changelog
