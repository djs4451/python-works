from app import generate_system_info

def test_hostname_exists():

    report = generate_system_info()

    assert "Hostname" in report


def test_os_exists():

    report = generate_system_info()

    assert "OS" in report


def test_timestamp_exists():

    report = generate_system_info()

    assert "Timestamp" in report
