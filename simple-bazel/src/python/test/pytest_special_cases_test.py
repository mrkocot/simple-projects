import pytest

def test_that_will_fail_with_cache_provider(request):
    # will fail if pytest does not get "-p no:cacheprovider"
    assert not request.config.pluginmanager.hasplugin("cacheprovider")

if __name__ == "__main__":
    pytest.main()
