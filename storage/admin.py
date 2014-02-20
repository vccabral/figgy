from django.contrib import admin

from storage.models import Book, Identifier


class InlineIdentifierAdmin(admin.StackedInline):
    model = Identifier
    extra = 0


class BookAdmin(admin.ModelAdmin):
    inlines = [InlineIdentifierAdmin]

    list_display = ['identifier', 'title', 'list_ids']

    def list_ids(self, obj):
        if obj:
            return '<br/>'.join([o.identifier for o in obj.identifiers.all()])

    list_ids.allow_tags = True



admin.site.register(Book, BookAdmin)


