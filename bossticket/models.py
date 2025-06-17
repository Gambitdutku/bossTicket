# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Search(models.Model):
    object_type = models.CharField(primary_key=True, max_length=8)  # The composite primary key (object_type, object_id) found, that is not supported. The first column is selected.
    object_id = models.PositiveIntegerField()
    title = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ost__search'
        unique_together = (('object_type', 'object_id'),)


class ApiKey(models.Model):
    isactive = models.IntegerField()
    ipaddr = models.CharField(max_length=64)
    apikey = models.CharField(unique=True, max_length=255)
    can_create_tickets = models.PositiveIntegerField()
    can_exec_cron = models.PositiveIntegerField()
    notes = models.TextField(blank=True, null=True)
    updated = models.DateTimeField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_api_key'


class Attachment(models.Model):
    object_id = models.PositiveIntegerField()
    type = models.CharField(max_length=1)
    file_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    inline = models.PositiveIntegerField()
    lang = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ost_attachment'
        unique_together = (('file_id', 'object_id'), ('object_id', 'file_id', 'type'),)


class CannedResponse(models.Model):
    canned_id = models.AutoField(primary_key=True)
    dept_id = models.PositiveIntegerField()
    isenabled = models.PositiveIntegerField()
    title = models.CharField(unique=True, max_length=255)
    response = models.TextField()
    lang = models.CharField(max_length=16)
    notes = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_canned_response'


class Config(models.Model):
    namespace = models.CharField(max_length=64)
    key = models.CharField(max_length=64)
    value = models.TextField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_config'
        unique_together = (('namespace', 'key'),)


class Content(models.Model):
    isactive = models.PositiveIntegerField()
    type = models.CharField(max_length=32)
    name = models.CharField(unique=True, max_length=255)
    body = models.TextField()
    notes = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_content'


class Department(models.Model):
    pid = models.PositiveIntegerField(blank=True, null=True)
    tpl_id = models.PositiveIntegerField()
    sla_id = models.PositiveIntegerField()
    schedule_id = models.PositiveIntegerField()
    email_id = models.PositiveIntegerField()
    autoresp_email_id = models.PositiveIntegerField()
    manager_id = models.PositiveIntegerField()
    flags = models.PositiveIntegerField()
    name = models.CharField(max_length=128)
    signature = models.TextField()
    ispublic = models.PositiveIntegerField()
    group_membership = models.IntegerField()
    ticket_auto_response = models.IntegerField()
    message_auto_response = models.IntegerField()
    path = models.CharField(max_length=128)
    updated = models.DateTimeField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_department'
        unique_together = (('name', 'pid'),)


class Draft(models.Model):
    staff_id = models.PositiveIntegerField()
    namespace = models.CharField(max_length=32)
    body = models.TextField()
    extra = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ost_draft'


class Email(models.Model):
    email_id = models.AutoField(primary_key=True)
    noautoresp = models.PositiveIntegerField()
    priority_id = models.PositiveIntegerField()
    dept_id = models.PositiveIntegerField()
    topic_id = models.PositiveIntegerField()
    email = models.CharField(unique=True, max_length=255)
    name = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_email'


class EmailAccount(models.Model):
    email_id = models.PositiveIntegerField()
    type = models.CharField(max_length=7)
    auth_bk = models.CharField(max_length=128)
    auth_id = models.CharField(max_length=16, blank=True, null=True)
    active = models.PositiveIntegerField()
    host = models.CharField(max_length=128)
    port = models.IntegerField()
    folder = models.CharField(max_length=255, blank=True, null=True)
    protocol = models.CharField(max_length=5)
    encryption = models.CharField(max_length=4)
    fetchfreq = models.PositiveIntegerField()
    fetchmax = models.PositiveIntegerField(blank=True, null=True)
    postfetch = models.CharField(max_length=7)
    archivefolder = models.CharField(max_length=255, blank=True, null=True)
    allow_spoofing = models.PositiveIntegerField(blank=True, null=True)
    num_errors = models.PositiveIntegerField()
    last_error_msg = models.TextField(blank=True, null=True)
    last_error = models.DateTimeField(blank=True, null=True)
    last_activity = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_email_account'


class EmailTemplate(models.Model):
    tpl_id = models.PositiveIntegerField()
    code_name = models.CharField(max_length=32)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    notes = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_email_template'
        unique_together = (('tpl_id', 'code_name'),)


class EmailTemplateGroup(models.Model):
    tpl_id = models.AutoField(primary_key=True)
    isactive = models.PositiveIntegerField()
    name = models.CharField(max_length=32)
    lang = models.CharField(max_length=16)
    notes = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_email_template_group'


class Event(models.Model):
    name = models.CharField(unique=True, max_length=60)
    description = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ost_event'


class Faq(models.Model):
    faq_id = models.AutoField(primary_key=True)
    category_id = models.PositiveIntegerField()
    ispublished = models.PositiveIntegerField()
    question = models.CharField(unique=True, max_length=255)
    answer = models.TextField()
    keywords = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_faq'


class FaqCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_pid = models.PositiveIntegerField(blank=True, null=True)
    ispublic = models.PositiveIntegerField()
    name = models.CharField(max_length=125, blank=True, null=True)
    description = models.TextField()
    notes = models.TextField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_faq_category'


class FaqTopic(models.Model):
    faq_id = models.PositiveIntegerField(primary_key=True)  # The composite primary key (faq_id, topic_id) found, that is not supported. The first column is selected.
    topic_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ost_faq_topic'
        unique_together = (('faq_id', 'topic_id'),)


class File(models.Model):
    ft = models.CharField(max_length=1)
    bk = models.CharField(max_length=1)
    type = models.CharField(max_length=255, db_collation='ascii_general_ci')
    size = models.PositiveBigIntegerField()
    key = models.CharField(max_length=86, db_collation='ascii_general_ci')
    signature = models.CharField(max_length=86, db_collation='ascii_bin')
    name = models.CharField(max_length=255)
    attrs = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_file'


class FileChunk(models.Model):
    file_id = models.IntegerField(primary_key=True)  # The composite primary key (file_id, chunk_id) found, that is not supported. The first column is selected.
    chunk_id = models.IntegerField()
    filedata = models.TextField()

    class Meta:
        managed = False
        db_table = 'ost_file_chunk'
        unique_together = (('file_id', 'chunk_id'),)


class Filter(models.Model):
    execorder = models.PositiveIntegerField()
    isactive = models.PositiveIntegerField()
    flags = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveIntegerField()
    match_all_rules = models.PositiveIntegerField()
    stop_onmatch = models.PositiveIntegerField()
    target = models.CharField(max_length=5)
    email_id = models.PositiveIntegerField()
    name = models.CharField(max_length=32)
    notes = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_filter'


class FilterAction(models.Model):
    filter_id = models.PositiveIntegerField()
    sort = models.PositiveIntegerField()
    type = models.CharField(max_length=24)
    configuration = models.TextField(blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_filter_action'


class FilterRule(models.Model):
    filter_id = models.PositiveIntegerField()
    what = models.CharField(max_length=32)
    how = models.CharField(max_length=10)
    val = models.CharField(max_length=255)
    isactive = models.PositiveIntegerField()
    notes = models.TextField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_filter_rule'
        unique_together = (('filter_id', 'what', 'how', 'val'),)


class Form(models.Model):
    pid = models.PositiveIntegerField(blank=True, null=True)
    type = models.CharField(max_length=8)
    flags = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    instructions = models.CharField(max_length=512, blank=True, null=True)
    name = models.CharField(max_length=64)
    notes = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_form'


class FormEntry(models.Model):
    form_id = models.PositiveIntegerField()
    object_id = models.PositiveIntegerField(blank=True, null=True)
    object_type = models.CharField(max_length=1)
    sort = models.PositiveIntegerField()
    extra = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_form_entry'


class FormEntryValues(models.Model):
    entry_id = models.PositiveIntegerField(primary_key=True)  # The composite primary key (entry_id, field_id) found, that is not supported. The first column is selected.
    field_id = models.PositiveIntegerField()
    value = models.TextField(blank=True, null=True)
    value_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ost_form_entry_values'
        unique_together = (('entry_id', 'field_id'),)


class FormField(models.Model):
    form_id = models.PositiveIntegerField()
    flags = models.PositiveIntegerField(blank=True, null=True)
    type = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    name = models.CharField(max_length=64)
    configuration = models.TextField(blank=True, null=True)
    sort = models.PositiveIntegerField()
    hint = models.CharField(max_length=512, blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_form_field'


class Group(models.Model):
    role_id = models.PositiveIntegerField()
    flags = models.PositiveIntegerField()
    name = models.CharField(max_length=120)
    notes = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_group'


class HelpTopic(models.Model):
    topic_id = models.AutoField(primary_key=True)
    topic_pid = models.PositiveIntegerField()
    ispublic = models.PositiveIntegerField()
    noautoresp = models.PositiveIntegerField()
    flags = models.PositiveIntegerField(blank=True, null=True)
    status_id = models.PositiveIntegerField()
    priority_id = models.PositiveIntegerField()
    dept_id = models.PositiveIntegerField()
    staff_id = models.PositiveIntegerField()
    team_id = models.PositiveIntegerField()
    sla_id = models.PositiveIntegerField()
    page_id = models.PositiveIntegerField()
    sequence_id = models.PositiveIntegerField()
    sort = models.PositiveIntegerField()
    topic = models.CharField(max_length=128)
    number_format = models.CharField(max_length=32, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_help_topic'
        unique_together = (('topic', 'topic_pid'),)


class HelpTopicForm(models.Model):
    topic_id = models.PositiveIntegerField()
    form_id = models.PositiveIntegerField()
    sort = models.PositiveIntegerField()
    extra = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ost_help_topic_form'


class List(models.Model):
    name = models.CharField(max_length=255)
    name_plural = models.CharField(max_length=255, blank=True, null=True)
    sort_mode = models.CharField(max_length=7)
    masks = models.PositiveIntegerField()
    type = models.CharField(max_length=16, blank=True, null=True)
    configuration = models.TextField()
    notes = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_list'


class ListItems(models.Model):
    list_id = models.IntegerField(blank=True, null=True)
    status = models.PositiveIntegerField()
    value = models.CharField(max_length=255)
    extra = models.CharField(max_length=255, blank=True, null=True)
    sort = models.IntegerField()
    properties = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ost_list_items'


class Lock(models.Model):
    lock_id = models.AutoField(primary_key=True)
    staff_id = models.PositiveIntegerField()
    expire = models.DateTimeField(blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_lock'


class Note(models.Model):
    pid = models.PositiveIntegerField(blank=True, null=True)
    staff_id = models.PositiveIntegerField()
    ext_id = models.CharField(max_length=10, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    status = models.PositiveIntegerField()
    sort = models.PositiveIntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_note'


class Organization(models.Model):
    name = models.CharField(max_length=128)
    manager = models.CharField(max_length=16)
    status = models.PositiveIntegerField()
    domain = models.CharField(max_length=256)
    extra = models.TextField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ost_organization'


class OrganizationCdata(models.Model):
    org_id = models.PositiveIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    website = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ost_organization__cdata'


class Plugin(models.Model):
    name = models.CharField(max_length=255)
    install_path = models.CharField(unique=True, max_length=60)
    isphar = models.IntegerField()
    isactive = models.IntegerField()
    version = models.CharField(max_length=64, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    installed = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_plugin'


class PluginInstance(models.Model):
    plugin_id = models.PositiveIntegerField()
    flags = models.IntegerField()
    name = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ost_plugin_instance'


class Queue(models.Model):
    parent_id = models.PositiveIntegerField()
    columns_id = models.PositiveIntegerField(blank=True, null=True)
    sort_id = models.PositiveIntegerField(blank=True, null=True)
    flags = models.PositiveIntegerField()
    staff_id = models.PositiveIntegerField()
    sort = models.PositiveIntegerField()
    title = models.CharField(max_length=60, blank=True, null=True)
    config = models.TextField(blank=True, null=True)
    filter = models.CharField(max_length=64, blank=True, null=True)
    root = models.CharField(max_length=32, blank=True, null=True)
    path = models.CharField(max_length=80)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_queue'


class QueueColumn(models.Model):
    flags = models.PositiveIntegerField()
    name = models.CharField(max_length=64)
    primary = models.CharField(max_length=64)
    secondary = models.CharField(max_length=64, blank=True, null=True)
    filter = models.CharField(max_length=32, blank=True, null=True)
    truncate = models.CharField(max_length=16, blank=True, null=True)
    annotations = models.TextField(blank=True, null=True)
    conditions = models.TextField(blank=True, null=True)
    extra = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ost_queue_column'


class QueueColumns(models.Model):
    queue_id = models.PositiveIntegerField(primary_key=True)  # The composite primary key (queue_id, column_id, staff_id) found, that is not supported. The first column is selected.
    column_id = models.PositiveIntegerField()
    staff_id = models.PositiveIntegerField()
    bits = models.PositiveIntegerField()
    sort = models.PositiveIntegerField()
    heading = models.CharField(max_length=64, blank=True, null=True)
    width = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ost_queue_columns'
        unique_together = (('queue_id', 'column_id', 'staff_id'),)


class QueueConfig(models.Model):
    queue_id = models.PositiveIntegerField(primary_key=True)  # The composite primary key (queue_id, staff_id) found, that is not supported. The first column is selected.
    staff_id = models.PositiveIntegerField()
    setting = models.TextField(blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_queue_config'
        unique_together = (('queue_id', 'staff_id'),)


class QueueExport(models.Model):
    queue_id = models.PositiveIntegerField()
    path = models.CharField(max_length=64)
    heading = models.CharField(max_length=64, blank=True, null=True)
    sort = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ost_queue_export'


class QueueSort(models.Model):
    root = models.CharField(max_length=32, blank=True, null=True)
    name = models.CharField(max_length=64)
    columns = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ost_queue_sort'


class QueueSorts(models.Model):
    queue_id = models.PositiveIntegerField(primary_key=True)  # The composite primary key (queue_id, sort_id) found, that is not supported. The first column is selected.
    sort_id = models.PositiveIntegerField()
    bits = models.PositiveIntegerField()
    sort = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ost_queue_sorts'
        unique_together = (('queue_id', 'sort_id'),)


class Role(models.Model):
    flags = models.PositiveIntegerField()
    name = models.CharField(unique=True, max_length=64, blank=True, null=True)
    permissions = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_role'


class Schedule(models.Model):
    flags = models.PositiveIntegerField()
    name = models.CharField(max_length=255)
    timezone = models.CharField(max_length=64, blank=True, null=True)
    description = models.CharField(max_length=255)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_schedule'


class ScheduleEntry(models.Model):
    schedule_id = models.PositiveIntegerField()
    flags = models.PositiveIntegerField()
    sort = models.PositiveIntegerField()
    name = models.CharField(max_length=255)
    repeats = models.CharField(max_length=16)
    starts_on = models.DateField(blank=True, null=True)
    starts_at = models.TimeField(blank=True, null=True)
    ends_on = models.DateField(blank=True, null=True)
    ends_at = models.TimeField(blank=True, null=True)
    stops_on = models.DateTimeField(blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)
    week = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_schedule_entry'


class Sequence(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    flags = models.PositiveIntegerField(blank=True, null=True)
    next = models.PositiveBigIntegerField()
    increment = models.IntegerField(blank=True, null=True)
    padding = models.CharField(max_length=1, blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_sequence'


class Session(models.Model):
    session_id = models.CharField(primary_key=True, max_length=255, db_collation='ascii_general_ci')
    session_data = models.TextField(blank=True, null=True)
    session_expire = models.DateTimeField(blank=True, null=True)
    session_updated = models.DateTimeField(blank=True, null=True)
    user_id = models.CharField(max_length=16, db_comment='osTicket staff/client ID')
    user_ip = models.CharField(max_length=64)
    user_agent = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ost_session'


class Sla(models.Model):
    schedule_id = models.PositiveIntegerField()
    flags = models.PositiveIntegerField()
    grace_period = models.PositiveIntegerField()
    name = models.CharField(unique=True, max_length=64)
    notes = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_sla'


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    dept_id = models.PositiveIntegerField()
    role_id = models.PositiveIntegerField()
    username = models.CharField(unique=True, max_length=32)
    firstname = models.CharField(max_length=32, blank=True, null=True)
    lastname = models.CharField(max_length=32, blank=True, null=True)
    passwd = models.CharField(max_length=128, blank=True, null=True)
    backend = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=24)
    phone_ext = models.CharField(max_length=6, blank=True, null=True)
    mobile = models.CharField(max_length=24)
    signature = models.TextField()
    lang = models.CharField(max_length=16, blank=True, null=True)
    timezone = models.CharField(max_length=64, blank=True, null=True)
    locale = models.CharField(max_length=16, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    isactive = models.IntegerField()
    isadmin = models.IntegerField()
    isvisible = models.PositiveIntegerField()
    onvacation = models.PositiveIntegerField()
    assigned_only = models.PositiveIntegerField()
    show_assigned_tickets = models.PositiveIntegerField()
    change_passwd = models.PositiveIntegerField()
    max_page_size = models.PositiveIntegerField()
    auto_refresh_rate = models.PositiveIntegerField()
    default_signature_type = models.CharField(max_length=4)
    default_paper_size = models.CharField(max_length=6)
    extra = models.TextField(blank=True, null=True)
    permissions = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    lastlogin = models.DateTimeField(blank=True, null=True)
    passwdreset = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_staff'


class StaffDeptAccess(models.Model):
    staff_id = models.PositiveIntegerField(primary_key=True)  # The composite primary key (staff_id, dept_id) found, that is not supported. The first column is selected.
    dept_id = models.PositiveIntegerField()
    role_id = models.PositiveIntegerField()
    flags = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ost_staff_dept_access'
        unique_together = (('staff_id', 'dept_id'),)


class Syslog(models.Model):
    log_id = models.AutoField(primary_key=True)
    log_type = models.CharField(max_length=7)
    title = models.CharField(max_length=255)
    log = models.TextField()
    logger = models.CharField(max_length=64)
    ip_address = models.CharField(max_length=64)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_syslog'


class Task(models.Model):
    object_id = models.IntegerField()
    object_type = models.CharField(max_length=1)
    number = models.CharField(max_length=20, blank=True, null=True)
    dept_id = models.PositiveIntegerField()
    staff_id = models.PositiveIntegerField()
    team_id = models.PositiveIntegerField()
    lock_id = models.PositiveIntegerField()
    flags = models.PositiveIntegerField()
    duedate = models.DateTimeField(blank=True, null=True)
    closed = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_task'


class TaskCdata(models.Model):
    task_id = models.PositiveIntegerField(primary_key=True)
    title = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ost_task__cdata'


class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    lead_id = models.PositiveIntegerField()
    flags = models.PositiveIntegerField()
    name = models.CharField(unique=True, max_length=125)
    notes = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_team'


class TeamMember(models.Model):
    team_id = models.PositiveIntegerField(primary_key=True)  # The composite primary key (team_id, staff_id) found, that is not supported. The first column is selected.
    staff_id = models.PositiveIntegerField()
    flags = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ost_team_member'
        unique_together = (('team_id', 'staff_id'),)


class Thread(models.Model):
    object_id = models.PositiveIntegerField()
    object_type = models.CharField(max_length=1)
    extra = models.TextField(blank=True, null=True)
    lastresponse = models.DateTimeField(blank=True, null=True)
    lastmessage = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_thread'


class ThreadCollaborator(models.Model):
    flags = models.PositiveIntegerField()
    thread_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    role = models.CharField(max_length=1)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_thread_collaborator'
        unique_together = (('thread_id', 'user_id'),)


class ThreadEntry(models.Model):
    pid = models.PositiveIntegerField()
    thread_id = models.PositiveIntegerField()
    staff_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    type = models.CharField(max_length=1)
    flags = models.PositiveIntegerField()
    poster = models.CharField(max_length=128)
    editor = models.PositiveIntegerField(blank=True, null=True)
    editor_type = models.CharField(max_length=1, blank=True, null=True)
    source = models.CharField(max_length=32)
    title = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField()
    format = models.CharField(max_length=16)
    ip_address = models.CharField(max_length=64)
    extra = models.TextField(blank=True, null=True)
    recipients = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_thread_entry'


class ThreadEntryEmail(models.Model):
    thread_entry_id = models.PositiveIntegerField()
    email_id = models.PositiveIntegerField(blank=True, null=True)
    mid = models.CharField(max_length=255)
    headers = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ost_thread_entry_email'


class ThreadEntryMerge(models.Model):
    thread_entry_id = models.PositiveIntegerField()
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ost_thread_entry_merge'


class ThreadEvent(models.Model):
    thread_id = models.PositiveIntegerField()
    thread_type = models.CharField(max_length=1)
    event_id = models.PositiveIntegerField(blank=True, null=True)
    staff_id = models.PositiveIntegerField()
    team_id = models.PositiveIntegerField()
    dept_id = models.PositiveIntegerField()
    topic_id = models.PositiveIntegerField()
    data = models.CharField(max_length=1024, blank=True, null=True, db_comment='Encoded differences')
    username = models.CharField(max_length=128)
    uid = models.PositiveIntegerField(blank=True, null=True)
    uid_type = models.CharField(max_length=1)
    annulled = models.PositiveIntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_thread_event'


class ThreadReferral(models.Model):
    thread_id = models.PositiveIntegerField()
    object_id = models.PositiveIntegerField()
    object_type = models.CharField(max_length=1)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_thread_referral'
        unique_together = (('object_id', 'object_type', 'thread_id'),)


class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    ticket_pid = models.PositiveIntegerField(blank=True, null=True)
    number = models.CharField(max_length=20, blank=True, null=True)
    user_id = models.PositiveIntegerField()
    user_email_id = models.PositiveIntegerField()
    status_id = models.PositiveIntegerField()
    dept_id = models.PositiveIntegerField()
    sla_id = models.PositiveIntegerField()
    topic_id = models.PositiveIntegerField()
    staff_id = models.PositiveIntegerField()
    team_id = models.PositiveIntegerField()
    email_id = models.PositiveIntegerField()
    lock_id = models.PositiveIntegerField()
    flags = models.PositiveIntegerField()
    sort = models.PositiveIntegerField()
    ip_address = models.CharField(max_length=64)
    source = models.CharField(max_length=5)
    source_extra = models.CharField(max_length=40, blank=True, null=True)
    isoverdue = models.PositiveIntegerField()
    isanswered = models.PositiveIntegerField()
    duedate = models.DateTimeField(blank=True, null=True)
    est_duedate = models.DateTimeField(blank=True, null=True)
    reopened = models.DateTimeField(blank=True, null=True)
    closed = models.DateTimeField(blank=True, null=True)
    lastupdate = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_ticket'


class TicketCdata(models.Model):
    ticket_id = models.PositiveIntegerField(primary_key=True)
    subject = models.TextField(blank=True, null=True)
    priority = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ost_ticket__cdata'


class TicketPriority(models.Model):
    priority_id = models.AutoField(primary_key=True)
    priority = models.CharField(unique=True, max_length=60)
    priority_desc = models.CharField(max_length=30)
    priority_color = models.CharField(max_length=7)
    priority_urgency = models.PositiveIntegerField()
    ispublic = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ost_ticket_priority'


class TicketStatus(models.Model):
    name = models.CharField(unique=True, max_length=60)
    state = models.CharField(max_length=16, blank=True, null=True)
    mode = models.PositiveIntegerField()
    flags = models.PositiveIntegerField()
    sort = models.PositiveIntegerField()
    properties = models.TextField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_ticket_status'


class Translation(models.Model):
    object_hash = models.CharField(max_length=16, db_collation='ascii_general_ci', blank=True, null=True)
    type = models.CharField(max_length=8, blank=True, null=True)
    flags = models.PositiveIntegerField()
    revision = models.PositiveIntegerField(blank=True, null=True)
    agent_id = models.PositiveIntegerField()
    lang = models.CharField(max_length=16)
    text = models.TextField()
    source_text = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ost_translation'


class User(models.Model):
    org_id = models.PositiveIntegerField()
    default_email_id = models.IntegerField()
    status = models.PositiveIntegerField()
    name = models.CharField(max_length=128)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_user'


class UserCdata(models.Model):
    user_id = models.PositiveIntegerField(primary_key=True)
    email = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ost_user__cdata'


class UserAccount(models.Model):
    user_id = models.PositiveIntegerField()
    status = models.PositiveIntegerField()
    timezone = models.CharField(max_length=64, blank=True, null=True)
    lang = models.CharField(max_length=16, blank=True, null=True)
    username = models.CharField(unique=True, max_length=64, blank=True, null=True)
    passwd = models.CharField(max_length=128, db_collation='ascii_bin', blank=True, null=True)
    backend = models.CharField(max_length=32, blank=True, null=True)
    extra = models.TextField(blank=True, null=True)
    registered = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ost_user_account'


class UserEmail(models.Model):
    user_id = models.PositiveIntegerField()
    flags = models.PositiveIntegerField()
    address = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'ost_user_email'
