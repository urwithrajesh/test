Name:           nodejsapp
Version:        1.0
Release:        0
Summary:        Dummy Project for CICD PipeLine 

Group:          Group
License:        License
URL:            somewebsite
Distribution:   Linux CentOS
Source0:        %{name}-%{version}.tar.gz

%description
CDR Platform is awesome product.


%prep

%setup -q

%build
/var/lib/jenkins/.nvm/versions/node/v8.5.0/bin/npm  install

%install
mkdir -p $RPM_BUILD_ROOT/appl/node
cp -pr *  $RPM_BUILD_ROOT/appl/node
install -m 755 -d $RPM_BUILD_ROOT/appl/node

%clean
rm -rf $RPM_BUILD_ROOT


%files
/appl/node/*
%defattr(-,root,root,-)
