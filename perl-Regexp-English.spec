%include	/usr/lib/rpm/macros.perl
%define	pdir	Regexp
%define	pnam	English
Summary:	Regexp::English perl module - create regular expressions more verbosely
Summary(pl):	Modu� perla Regexp::English - do bardziej rozwlek�ych wyra�e� regularnych
Name:		perl-Regexp-English
Version:	0.21
Release:	2
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	63ccfbe00390edf169c2bc89901da81a
BuildRequires:	perl-devel >= 5.6
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
Modu� Regexp::English daje alternatywn� sk�adni� wyra�e� regularnych,
kt�ra jest nieco wi�cej m�wi�ca ni� standardowe mechanizmy. Dodatkowo
daje kilka wygodnych mo�liwo�ci, takich jak przyrostowe budowanie
wyra�e� i wychwytywanie ogranicze�.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

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
