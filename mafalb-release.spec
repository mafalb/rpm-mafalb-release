Name: mafalb-release          
Version:        0.0
Release:        1%{?dist}
Summary:        mafalb repo release
License:        GPLv3
Source0:        RPM-GPG-KEY-mafalb-20170318
Source1:        mafalb.repo
Packager:       Markus Falb <rpm@mafalb.at>

%description
mafalb repo release


%prep

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/etc/pki/rpm-gpg
mkdir -p %{buildroot}/etc/yum.repos.d

cp RPM-GPG-KEY-mafalb-20170318 %{buildroot}/etc/pki/rpm-gpg/RPM-GPG-KEY-mafalb-20170318
cp mafalb.repo %{buildroot}/etc/yum.repos.d/mafalb.repo

%clean
rm -rf %{buildroot}

%files
%doc

%defattr (0644, root, root, 0755)
/etc/pki/rpm-gpg/RPM-GPG-KEY-mafalb-20170318
%config(noreplace) /etc/yum.repos.d/mafalb.repo


%changelog
* Tue Nov 29 2016 Markus Falb <rpm@mafalb.at>
- initial rpm build