#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Regexp
%define		pnam	English
Summary:	Regexp::English Perl module - create regular expressions more verbosely
Summary(pl):	Modu³ Perla Regexp::English - tworzenie bardziej rozwlek³ych wyra¿eñ regularnych
Name:		perl-Regexp-English
Version:	1.00
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a45458c387580d731f192469a694bfc0
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Test-Simple >= 0.30
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Regexp::English provides an alternate regular expression syntax, one
that is slightly more verbose than the standard mechanisms. In
addition, it adds a few convenient features, like incremental
expression building and bound captures.

%description -l pl
Modu³ Regexp::English daje alternatywn± sk³adniê wyra¿eñ regularnych,
która jest nieco wiêcej mówi±ca ni¿ standardowe mechanizmy. Dodatkowo
daje kilka wygodnych mo¿liwo¶ci, takich jak przyrostowe budowanie
wyra¿eñ i wychwytywanie ograniczeñ.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Regexp/English.pm
%{_mandir}/man3/*
