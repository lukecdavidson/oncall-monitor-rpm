Name:           oncall-monitor
Version:        0.0.2
Release:        1%{?dist}
Summary:        A service to monitor for microphone input and play an alarm on detection
BuildArch:      noarch

License:        GPL
Source0:        %{name}-%{version}.tar.gz

Requires:       bash
Requires:       systemd

%description
A service to monitor for microphone input and play an alarm on detection


%prep
%setup -q


%install
mkdir -pv %{buildroot}/usr/bin
mkdir -pv %{buildroot}/usr/lib/systemd/user
install -vm 755 oncall %{buildroot}/usr/bin/oncall
install -vm 755 oncall-monitor %{buildroot}/usr/bin/oncall-monitor
install -vm 644 oncall-monitor.service %{buildroot}/usr/lib/systemd/user/oncall-monitor.service
install -vm 644 oncall-monitor.timer %{buildroot}/usr/lib/systemd/user/oncall-monitor.timer


%clean
rm -rf $RPM_BUILD_ROOT


%files
/usr/bin/oncall
/usr/bin/oncall-monitor
/usr/lib/systemd/user/oncall-monitor.service
/usr/lib/systemd/user/oncall-monitor.timer


%changelog
* Tue Feb 21 2023 Luke Davidson <luke@lukedavidson.org>
- 0.0.1
- First version packaged 
