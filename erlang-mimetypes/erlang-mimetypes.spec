%global realname mimetypes
%global upstream spawngrid
%global debug_package %{nil}
%global git_tag d42a72a
%global patchnumber 0


Name:		erlang-%{realname}
Version:	0.9
Release:	1%{?dist}
Summary:	An Erlang library to fetch MIME extension/name mappings
Group:		Development/Libraries
License:	Freely redistributable without restriction
URL:		https://github.com/spawngrid/mimetypes
# wget --content-disposition https://github.com/spawngrid/mimetypes/tarball/d42a72a
Source0:	%{upstream}-%{realname}-%{version}-%{patchnumber}-g%{git_tag}.tar.gz
Patch1:		erlang-mimetypes-0001-Replace-git-vsn-with-fixed-value.patch
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:	erlang-rebar
Requires:	erlang-erts >= R14B
Requires:	erlang-kernel >= R14B
Requires:	erlang-stdlib >= R14B


%description
mimetypes is an Erlang library to fetch MIME extension/name mappings.


%prep
%setup -q -n %{upstream}-%{realname}-%{git_tag}
%patch1 -p1

%build
rebar compile -v


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/erlang/lib/%{realname}-%{version}/ebin
mkdir -p %{buildroot}%{_libdir}/erlang/lib/%{realname}-%{version}/priv
install -m 644 ebin/%{realname}.app %{buildroot}%{_libdir}/erlang/lib/%{realname}-%{version}/ebin
install -m 644 ebin/*.beam %{buildroot}%{_libdir}/erlang/lib/%{realname}-%{version}/ebin
install -m 644 priv/mime.types %{buildroot}%{_libdir}/erlang/lib/%{realname}-%{version}/priv

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%dir %{_libdir}/erlang/lib/%{realname}-%{version}
%dir %{_libdir}/erlang/lib/%{realname}-%{version}/ebin
%dir %{_libdir}/erlang/lib/%{realname}-%{version}/priv
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/%{realname}.app
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/*.beam
%{_libdir}/erlang/lib/%{realname}-%{version}/priv/mime.types

%changelog
* Mon Nov 28 2012 Jan Vincent Liwanag <jvliwanag@gmail.com>
- Initial release