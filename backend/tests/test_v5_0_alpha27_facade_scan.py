from app.v500_alpha27_scanner.service import ScannerFacadeV500Alpha27

def test_v500_alpha27_facade_scan(): assert ScannerFacadeV500Alpha27().scan()['accepted'] == 2
