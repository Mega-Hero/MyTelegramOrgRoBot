#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) Shrimadhav U K
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


class Translation:
    START_TEXT = (
        "Hi!\n"
        "మీరు తప్పనిసరిగా బోట్ యొక్క నియమాలు మరియు షరతులను చదవాలి https://telegra.ph/My-Telegram-ORG-06-12\n"
        "నన్ను ఉపయోగించినందుకు ధన్యవాదాలు 😬\n"
        "మీ టెలిగ్రామ్ ఫోన్ నంబర్‌ను నమోదు చేయండి, "
        "నుండి APP-IDని పొందడానికి my.telegram.org\n\n"
        "/start ఏ దశలోనైనా మీ వివరాలను మళ్లీ నమోదు చేయండి @MutyalHarshith"
    )
    AFTER_RECVD_CODE_TEXT = (
        "అలాగా!\n"
        "ఇప్పుడు దయచేసి టెలిగ్రామ్ కోడ్‌ని పంపండి "
        "మీరు టెలిగ్రామ్ కోడ్ నుండి అందుకున్నారు!\n\n"

        "ఈ కోడ్ ప్రయోజనం కోసం మాత్రమే ఉపయోగించబడుతుంది "
        "నుండి APP IDని పొందడం my.telegram.org\n"
        "మీరు ఈ బోట్ దేవ్‌ను విశ్వసించకపోతే, "
        "దయచేసి ఈ బోట్‌ను మీరే హోస్ట్ చేయండి\n"
        "తెరవడం ద్వారా https://telegra.ph/My-Telegram-ORG-06-12 and "
        "మమ్మల్ని అనుసరించు క్లిక్ చేయడం @MutyalaHarshith \n\n"

        "/start ఏ దశలోనైనా మీ వివరాలను మళ్లీ నమోదు చేయండి"
    )
    BEFORE_SUCC_LOGIN = "కోడ్ అందుకుంది. వెబ్ పేజీని స్క్రాప్ చేస్తోంది ..."
    ERRED_PAGE = "ఏదో తప్పు. యాప్ ఐడిని పొందడంలో విఫలమైంది. \n\n@MutyalaHarshith"
    CANCELLED_MESG = "బై! దయచేసి తిరిగి /start బోట్ సంభాషణ"
    IN_VALID_CODE_PVDED = (
        "క్షమించండి, "
        "కానీ ఇన్‌పుట్ కనిపించడం లేదు "
        "చెల్లుబాటు అయ్యే టెలిగ్రామ్ వెబ్-లాగిన్ కోడ్"
    )
    IN_VALID_PHNO_PVDED = (
        "క్షమించండి, "
        "కానీ ఇన్‌పుట్ కనిపించడం లేదు "
        "చెల్లుబాటు అయ్యే ఫోన్ నంబర్"
    )
