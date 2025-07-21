from celery import shared_task
from legalservice.models import (
    CaseTray,
    Emergency,
    DraftingAffidavit,
    DraftingAgreement,
    FamilyMatter,
    LabourLaw,
    LandMatter,
    LegalAdvice,
    OtherMatter,
)


@shared_task(name="Add case to inbox tray")
def add_case_to_tray(case_id: str, case_model: str) -> None:
    """Add incoming cases to tray"""

    case = CaseTray.objects.get(name="inbox")
    match case_model:
        case "Emergency":
            emergency = Emergency.objects.get(gid=case_id)
            case.emergency_set.add(emergency)
        case "DraftingAffidavit":
            affidavit = DraftingAffidavit.objects.get(gid=case_id)
            case.draftingaffidavit_set.add(affidavit)
        case "DraftingAgreement":
            drafting_agreement = DraftingAgreement.objects.get(gid=case_id)
            case.draftingagreement_set.add(drafting_agreement)
        case "FamilyMatter":
            family = FamilyMatter.objects.get(gid=case_id)
            case.familymatter_set.add(family)
        case "LabourLaw":
            labour_law = LabourLaw.objects.get(gid=case_id)
            case.labourlaw_set.add(labour_law)
        case "LandMatter":
            land_matter = LandMatter.objects.get(gid=case_id)
            case.landmatter_set.add(land_matter)
        case "LegalAdvice":
            legal_advice = LegalAdvice.objects.get(gid=case_id)
            case.legaladvice_set.add(legal_advice)
        case "OtherMatter":
            other_matter = OtherMatter.objects.get(gid=case_id)
            case.othermatter_set.add(other_matter)
        case _:
            pass
