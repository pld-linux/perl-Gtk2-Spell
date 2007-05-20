#
# TODO:
# - license, links
# - translations
# - BR-s and R-s
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Gtk2
%define	pnam	Spell
Summary:	Gtk2::Spell - Bindings for GtkSpell with Gtk2
#Summary(pl.UTF-8):	
Name:		perl-Gtk2-Spell
Version:	1.03
Release:	1
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Gtk2/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	caf3b6d1e48e4c9096b2ab1ee15cbf4d
URL:		http://search.cpan.org/~mlehmann/Gtk2-Spell-1.03/
BuildRequires:	gtkspell-devel
BuildRequires:	perl-ExtUtils-Depends
BuildRequires:	perl-ExtUtils-PkgConfig
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl bindings to GtkSpell, used in concert with Gtk2::TextView. Provides 
mis-spelled word highlighting in red and offers a right click pop-up menu with
suggested corrections.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%{perl_vendorarch}/Gtk2/*.pm
%dir %{perl_vendorarch}/auto/Gtk2/Spell
%{perl_vendorarch}/auto/Gtk2/Spell/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Gtk2/Spell/*.so
%{_mandir}/man3/*
