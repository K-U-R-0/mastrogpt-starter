import sys 
sys.path.append("packages/afar/reverse")
import reverse

def test_reverse():
    res = reverse.reverse({})
    assert res["output"] == "Please provide an input"
