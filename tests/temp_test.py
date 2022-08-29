class TaoBaoKeGoodsDAO:

    def __init__(self):
        try:
            self.session = sessionmaker(sqlite_engine)()
        except Exception as e:
            print('connect database failure', e)

    def __del__(self):
        self.session.close()

    # 新增
    def insert(self, tbk_good):
        self.session.add(tbk_good)
        self.session.commit()
        return tbk_good.id

    # 批量新增
    def insert_batch(self, tbk_good_array):
        self.session.add_all(tbk_good_array)
        self.session.commit()

    # 修改
    def update(self, goods_id, **kwargs):
        self.session.query(TaoBaoKeGoods).filter(TaoBaoKeGoods.id == goods_id).update(kwargs)
        self.session.commit()

    # 删除
    def delete_by_id(self, goods_id):
        self.session.query(TaoBaoKeGoods).filter(TaoBaoKeGoods.id == goods_id).delete()
        self.session.commit()

    # 读取一条
    def read_one(self):
        return self.session.query(TaoBaoKeGoods).first()

    # 根据ID读取一条
    def read_one_by_id(self, goods_id):
        return self.session.query(TaoBaoKeGoods).filter(TaoBaoKeGoods.id == goods_id).first()

    # 读取所有
    def read_all(self):
        return self.session.query(TaoBaoKeGoods).all()

    # 读取所有通过filter
    def read_all_by_filter(self, *filter_clauses):
        for filter_clause in filter_clauses:
            print(filter_clause)
        return self.session.query(TaoBaoKeGoods).filter(*filter_clauses).all()

    # 读取所有通过filter_by
    def read_all_by_filter_by(self, **filter_by_clauses):
        for filter_by_key in filter_by_clauses:
            print(filter_by_key, filter_by_clauses[filter_by_key])
        return self.session.query(TaoBaoKeGoods).filter_by(**filter_by_clauses).all()

    # 读取所有分页
    def read_all_pagination(self, *order_by_clauses, offset=0, limit=10):
        for order_by_clause in order_by_clauses:
            print(order_by_clause)
        return self.session.query(TaoBaoKeGoods).order_by(*order_by_clauses).offset(offset).limit(limit).all()


if __name__ == '__main__':
    Base.metadata.drop_all(sqlite_engine)

    TaoBaoKeGoods.create_database_table()

    taoBaoKeGoodDAO = TaoBaoKeGoodsDAO()

    taoBaoKeGoods1 = TaoBaoKeGoods(category_id=1, item_id=1, title="新增测试标题1", sub_title="新增测试子标题1")
    goodsId = taoBaoKeGoodDAO.insert(taoBaoKeGoods1)
    print('insert goods id :', goodsId)

    tmpTaoBaoKeGoods = taoBaoKeGoodDAO.read_one_by_id(goodsId)
    print('read one by id', tmpTaoBaoKeGoods.category_id, tmpTaoBaoKeGoods.item_id, tmpTaoBaoKeGoods.title,
          tmpTaoBaoKeGoods.sub_title)

    taoBaoKeGoods2 = TaoBaoKeGoods(category_id=1, item_id=2, title="新增测试标题2", sub_title="新增测试子标题2")
    taoBaoKeGoods3 = TaoBaoKeGoods(category_id=1, item_id=3, title="新增测试标题3", sub_title="新增测试子标题3")
    taoBaoKeGoodDAO.insert_batch([taoBaoKeGoods2, taoBaoKeGoods3])

    taoBaoKeGoodDAO.update(goods_id=goodsId, **{'title': '新增测试标题1修改', 'sub_title': '新增测试子标题1修改'})
    tmpTaoBaoKeGoods = taoBaoKeGoodDAO.read_one_by_id(goodsId)
    print('read one by id', tmpTaoBaoKeGoods.category_id, tmpTaoBaoKeGoods.item_id, tmpTaoBaoKeGoods.title, ' ',
          tmpTaoBaoKeGoods.sub_title)

    tmpTaoBaoKeGoods = taoBaoKeGoodDAO.read_one()
    print('read one', tmpTaoBaoKeGoods.category_id, tmpTaoBaoKeGoods.item_id, tmpTaoBaoKeGoods.title, ' ',
          tmpTaoBaoKeGoods.sub_title)

    for result in taoBaoKeGoodDAO.read_all():
        print('read all', result.category_id, result.item_id, result.title, ' ', result.sub_title)
        print(result.__dict__)

    for result in taoBaoKeGoodDAO.read_all_by_filter(*(TaoBaoKeGoods.category_id == 1, TaoBaoKeGoods.item_id > 1)):
        print('read all by filter', result.category_id, result.item_id, result.title, ' ', result.sub_title)

    for result in taoBaoKeGoodDAO.read_all_by_filter_by(**{'category_id': 1, 'item_id': 2}):
        print('read all by filter by', result.category_id, result.item_id, result.title, ' ', result.sub_title)

    for result in taoBaoKeGoodDAO.read_all_pagination(*(TaoBaoKeGoods.category_id.asc(), TaoBaoKeGoods.item_id.desc()),
                                                      offset=0, limit=2):
        print('read all pagination', result.category_id, result.item_id, result.title, ' ', result.sub_title)

    taoBaoKeGoodDAO.delete_by_id(goodsId)
    tmpTaoBaoKeGoods = taoBaoKeGoodDAO.read_one_by_id(goodsId)
    print('read one by id', tmpTaoBaoKeGoods)
