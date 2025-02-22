from pydantic_settings import BaseSettings, SettingsConfigDict
from version import __version__



class _MessageSetings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", case_sensitive=True, extra="ignore"
    )

    START_ADMIN: str = (
        "درود 🙌🏻\n"
        "به داشبورد مدیریت وال بات خوش آمدید.\n\n"
        "💻 devlop by: @primez_dev"
        f"🐋 wall bot {__version__}"
    )
    START_NONE_SUDO: str = (
        "درود 🙌🏻\n"
        "به پنل مدیریت کاربران ویتوری وال بات خوش آمدید.\n\n"
        f"🐋 wall bot {__version__}"
    )
    ADD_ADMIN_STEP1: str = (
        "1⃣ مرحله اول \n"
        "🚹 لطفا یک یوزر نیم یونیک (انگلیسی) وارد کنید:"
    )
    ADD_ADMIN_STEP2: str = (
        "2⃣ مرحله دوم \n"
        "🔑 لطفا یک پسورد یونیک (انگلیسی) وارد کنید:"
    )
    ADD_ADMIN_STEP3: str = (
        "3⃣ مرحله سوم \n"
        "🔋 لطفا مقدار ترافیک قابل استفاده (عدد انگلیسی) برای این نماینده وارد کنید:"
    )
    ADD_ADMIN_STEP4: str = (
        "4⃣ مرحله چهارم \n"
        "لطفا ایدی سطراینباند مدنظر (عدد انگلیسی) ، مختص این نماینده را وارد کنید:"
    )
    ADD_USER_STEP1: str = (
        "🚹 لطفا یک یوزر نیم یونیک وارد کنید:"
    )
    ADD_USER_STEP2: str = (
        "🔋 لطفا ترافیک قابل استفاده (عدد انگلیسی) بر حسب GB برای این کاربر را وارد کنید:"
    )
    ADD_USER_STEP3: str = (
        "⏳️ لطفا تعداد روز های قابل استفاده (عدد انگلیسی) برای این کاربر را وارد کنید:"
    )
    RENEW_SUER: str = (
        "⚠️ توجه \n"
        "‼️با تمدید کاربر مورد نظر ترافیک اون کاربر ریست خواهد شد اما تعداد روز های اشتراکش رو شما در مرحله بعدی تعیین میکنید.\n"
        "🔹درصورت تمایل نام کاربری مورد نظر رو وارد کنید:"
    )
    CHANGE_INB: str = (
        "⚠️ توجه \n"
        "‼️با تغییر اینباند یک نماینده کاربران قبلی اون دیگه براش نشون داده نمیشه ، درصورت نیاز میتونید از طریق خود پنل بصورت یکجا کاربرارو از اینباند قبلی کات و به اینباند جدید منتقل کنید.\n"
        "1⃣مرحله اول \n"
        "🚹 درصورت تمایل تعویض اینباند ، یوزرنیم نماینده مورد نظر رو وارد کنید:"
    )
    CONFIRM_REGIST: str = (
        "⚠️توجه شما در حال ثبت یوزر نیم پسورد و اینباند اختصاصی برای درخواست دهنده هستید اما نماینده بعد از لاگین در ربات جهت ساخت کاربر باید ترافیک خریداری کند.\n"
        "1⃣مرحله اول \n"
        "یوزنیم اختصاصی این نماینده را به انگلیسی ارسال کنید:"
    )
    ADD_PLAN_STEP1: str = (
        "1⃣مرحله اول \n"
        "ترافیک مورد نظر رو به گیگابایت وارد کنید:\n"
        "(برای مثال: 1000)"
    )
    ADD_PLAN_STEP2: str = (
        "2⃣ مرحله دوم:\n"
        "قیمت این پلن رو به تومان وارد کنید:\n"
        "(برای مثال: 800000)"
    )
    CHANGE_PLAN_STEP1: str = (
        "1⃣مرحله اول \n"
        "ایدی پلن مورد نظر رو وارد کنید:\n"
        "(برای مثال: 1)"
    )
    CHANGE_PLAN_STEP2: str = (
        "2⃣ مرحله دوم:\n"
        "ترافیک پلن رو وارد کنید:\n"
        "(برای مثال: 800000)"
    )
    CHANGE_PLAN_STEP3: str = (
        "3⃣ مرحله سوم:\n"
        "قیمت پلن رو به تومان وارد کنید:\n"
        "(برای مثال: 800000)"
    )
    DELETE_PLAN: str = (
        "⚠️ آیدی پلن مورد نظر رو جهت حذف کردن ارسال کنید:"
    )
    CARD_PAYMENT_MESSAGE: str = (
        "⚠️توجه \n"
        "لطفا تصویر فیش واریز رو بدون کپشن ارسال کنید\n"
    )
    WAITING_FOR_APPROV_CARD_PAYMENT: str = (
        "♻️ تصویر درحال پردازش است...\n"
        "(بزودی پس از تایید اطلاع رسانی خواهد شد)"
    )
    CONFIRM_CARD_PAYMENT: str = (
        "✅ پرداخت شما تایید شد!\n"
        "(اطلاعات کامل در بخش مشخصات من)"
    )

messages_setting = _MessageSetings()
