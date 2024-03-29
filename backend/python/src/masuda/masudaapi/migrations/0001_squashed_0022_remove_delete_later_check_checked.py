# Generated by Django 3.2.9 on 2022-10-28 08:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    replaces = [('masudaapi', '0001_initial'), ('masudaapi', '0002_auto_20220617_1457'), ('masudaapi', '0003_post_may_be_deleted'), ('masudaapi', '0004_auto_20220617_1930'), ('masudaapi', '0005_alter_bookmark_masuda_id'), ('masudaapi', '0006_auto_20220704_1855'), ('masudaapi', '0007_progress'), ('masudaapi', '0008_progress_service'), ('masudaapi', '0009_post_bookmark_count'), ('masudaapi', '0010_auto_20220722_1225'), ('masudaapi', '0011_auto_20220728_1257'), ('masudaapi', '0012_auto_20220802_1250'), ('masudaapi', '0013_rename_delete_list_delete_post'), ('masudaapi', '0014_delete_post_post'), ('masudaapi', '0015_auto_20220804_1303'), ('masudaapi', '0016_auto_20220805_1235'), ('masudaapi', '0017_auto_20220823_1550'), ('masudaapi', '0018_auto_20220912_1728'), ('masudaapi', '0019_delete_post_user'), ('masudaapi', '0020_auto_20221017_1540'), ('masudaapi', '0021_alter_delete_later_check_post'), ('masudaapi', '0022_remove_delete_later_check_checked')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HatenaUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hatena_id', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('masuda_id', models.CharField(max_length=200)),
                ('bookmark_count', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('masuda_id', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('posted_at', models.DateTimeField()),
                ('response_count', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masudaapi.hatenauser')),
            ],
        ),
        migrations.AddConstraint(
            model_name='hatenauser',
            constraint=models.UniqueConstraint(fields=('hatena_id',), name='unique_hatenauser_hatena_id'),
        ),
        migrations.AddConstraint(
            model_name='bookmark',
            constraint=models.UniqueConstraint(fields=('masuda_id',), name='unique_bookmark_masuda_id'),
        ),
        migrations.AddField(
            model_name='post',
            name='may_be_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='hatenauser',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='hatenauser',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddConstraint(
            model_name='post',
            constraint=models.UniqueConstraint(fields=('masuda_id',), name='unique_post_hatena_id'),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='masuda_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='post', to='masudaapi.post', to_field='masuda_id'),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='bookmark_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='masuda_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='bookmark', to='masudaapi.post', to_field='masuda_id'),
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(default=0)),
                ('processed', models.IntegerField(default=0)),
                ('action', models.SmallIntegerField(choices=[(1, '取り込み'), (2, '削除'), (3, 'Space masuda'), (4, '選択削除'), (5, '再読み込み')], default=0)),
                ('status', models.SmallIntegerField(choices=[(0, '処理待ち'), (1, '処理中'), (2, '処理済み'), (3, '停止'), (9, 'エラー')], default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('memo', models.TextField(blank=True, null=True)),
                ('overview', models.CharField(blank=True, max_length=200, null=True)),
                ('pid', models.CharField(blank=True, max_length=100, null=True)),
                ('pidfile', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='masudaapi.hatenauser')),
            ],
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='masuda_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='bookmark', to='masudaapi.post', to_field='masuda_id'),
        ),
        migrations.AddField(
            model_name='post',
            name='bookmark_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Delete_Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('masuda_id', models.CharField(max_length=200)),
                ('is_executed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('progress', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='delete_posts', to='masudaapi.progress')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='delete_posts', to='masudaapi.post')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='masudaapi.hatenauser')),
            ],
        ),
        migrations.CreateModel(
            name='StopCommand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_executed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('progress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stop_commands', to='masudaapi.progress')),
            ],
        ),
        migrations.DeleteModel(
            name='Bookmark',
        ),
        migrations.CreateModel(
            name='Delete_Later_Check',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='delete_later_check', to='masudaapi.post')),
            ],
        ),
    ]
