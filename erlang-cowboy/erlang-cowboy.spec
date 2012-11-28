%global realname cowboy
%global upstream extend
%global debug_package %{nil}
%global git_tag af07e04
%global patchnumber 0


Name:		erlang-%{realname}
Version:	0.6.1
Release:	1%{?dist}
Summary:	A small, fast and modular HTTP server written in Erlang
Group:		Development/Libraries
License:	Freely redistributable without restriction
URL:		https://github.com/extend/cowboy
# wget --content-disposition https://github.com/extend/cowboy/tarball/0.6.1
Source0:	%{upstream}-%{realname}-%{version}-%{patchnumber}-g%{git_tag}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:	erlang-rebar
Requires:	erlang-erts >= R14B
Requires:	erlang-kernel >= R14B
Requires:	erlang-stdlib >= R14B


%description
Cowboy is a small, fast and modular HTTP server written in Erlang


%prep
%setup -q -n %{upstream}-%{realname}-%{git_tag}

%build
rebar compile -v


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/erlang/lib/%{realname}-%{version}/ebin
mkdir -p %{buildroot}%{_libdir}/erlang/lib/%{realname}-%{version}/include
install -m 644 ebin/%{realname}.app %{buildroot}%{_libdir}/erlang/lib/%{realname}-%{version}/ebin
install -m 644 ebin/*.beam %{buildroot}%{_libdir}/erlang/lib/%{realname}-%{version}/ebin
install -m 644 include/http.hrl %{buildroot}%{_libdir}/erlang/lib/%{realname}-%{version}/include

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%dir %{_libdir}/erlang/lib/%{realname}-%{version}
%dir %{_libdir}/erlang/lib/%{realname}-%{version}/ebin
%dir %{_libdir}/erlang/lib/%{realname}-%{version}/include
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/%{realname}.app
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/*.beam
%{_libdir}/erlang/lib/%{realname}-%{version}/include/*.hrl

%changelog
* Mon Nov 26 2012 Jan Vincent Liwanag <jvliwanag@gmail.com>
- Initial release