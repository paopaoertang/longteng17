#coding:utf-8
import pytest
import pytest_check as ck


@pytest.mark.p1
@pytest.mark.api
def test_add_fuel_card_normal(base_url, db, data, api):
    url = base_url + '/gasStation/process'
    data_source_id = data.get('data_source_id')
    card_number = data.get('card_number')

    # 环境准备
    db.change_db(f'delete from cardinfo where cardNumber={card_number}')

    json_data = {"dataSourceId": data_source_id, "methodId": "00A",
                  "CardInfo": {"cardNumber": card_number}}
    res = api.post(url, json=json_data)
    res_dict = res.json()
    print(res_dict)
    ck.equal(200, res_dict.get("code"))
    ck.equal("添加卡成功", res_dict.get("msg"))
    ck.is_true()
# if __name__ == '__main__':
#     pytest.main(["test_add_fuel_card.py","-sq"])



