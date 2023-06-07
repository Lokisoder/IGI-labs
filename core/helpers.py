def create_meta(entity_model):
    class Meta:
        model = entity_model
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

    return Meta
