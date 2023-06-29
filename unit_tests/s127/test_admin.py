from s127.admin import AccumulatedInlines


class TestAccumulatedInlines:
    class ParentInline(AccumulatedInlines):
        inlines = [1, 2]

    class ChildInline(ParentInline):
        pass

    class GrandChildInline(ChildInline):
        inlines = [1, 3]

    def test_get_inlines(self):
        assert self.ParentInline().get_inlines() == [1, 2]

    def test_get_inlines_on_inherited_inline(self):
        assert self.ChildInline().get_inlines() == [1, 2]

    def test_get_inlines_with_accumulated_inlines(self):
        assert self.GrandChildInline().get_inlines() == [1, 3, 2]
