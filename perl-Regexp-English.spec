#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Regexp
%define		pnam	English
%include	/usr/lib/rpm/macros.perl
Summary:	Regexp::English Perl module - create regular expressions more verbosely
Summary(pl.UTF-8):	Moduł Perla Regexp::English - tworzenie bardziej rozwlekłych wyrażeń regularnych
Name:		perl-Regexp-English
Version:	1.01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4d388ced5149dd46d7c8613f937fe97a
URL:		http://search.cpan.org/dist/Regexp-English/
BuildRequires:	perl-Test-Simple >= 0.30
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Regexp::English provides an alternate regular expression syntax, one
that is slightly more verbose than the standard mechanisms. In
addition, it adds a few convenient features, like incremental
expression building and bound captures.

%description -l pl.UTF-8
Moduł Regexp::English daje alternatywną składnię wyrażeń regularnych,
która jest nieco więcej mówiąca niż standardowe mechanizmy. Dodatkowo
daje kilka wygodnych możliwości, takich jak przyrostowe budowanie
wyrażeń i wychwytywanie ograniczeń.

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
