import json

from django.urls import reverse
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.templatetags.static import static as resolve_static


# ── Error pages ──────────────────────────────────────────────────────────────
def handler404(request, exception):
    content = render_to_string('main/404.html', {}, request=request)
    return HttpResponse(content, status=404)


# ── Page Views ───────────────────────────────────────────────────────────────
class AboutView(TemplateView):
    template_name = 'main/about.html'

class AboutAboutAeronicaView(TemplateView):
    template_name = 'main/about/about-aeronica.html'

class AboutCareersView(TemplateView):
    template_name = 'main/about/careers.html'

class AboutCertificationsView(TemplateView):
    template_name = 'main/about/certifications.html'

class AboutLeadershipTeamView(TemplateView):
    template_name = 'main/about/leadership-team.html'

class AboutPartnersAlliancesView(TemplateView):
    template_name = 'main/about/partners-alliances.html'

class AboutTechnologyStackView(TemplateView):
    template_name = 'main/about/technology-stack.html'

class AboutWhyAeronicaView(TemplateView):
    template_name = 'main/about/why-aeronica.html'

class CaseStudiesView(TemplateView):
    template_name = 'main/case-studies.html'

class CaseStudiesAgricultureProjectsView(TemplateView):
    template_name = 'main/case-studies/agriculture-projects.html'

class CaseStudiesGovernmentProjectsView(TemplateView):
    template_name = 'main/case-studies/government-projects.html'

class CaseStudiesInfrastructureProjectsView(TemplateView):
    template_name = 'main/case-studies/infrastructure-projects.html'

class CaseStudiesLocustControlMaharashtraView(TemplateView):
    template_name = 'main/case-studies/locust-control-maharashtra.html'

class CaseStudiesMiningProjectsView(TemplateView):
    template_name = 'main/case-studies/mining-projects.html'

class CaseStudiesProjectGalleryView(TemplateView):
    template_name = 'main/case-studies/project-gallery.html'

class CaseStudiesSmartCityProjectsView(TemplateView):
    template_name = 'main/case-studies/smart-city-projects.html'

class CaseStudiesUtilityProjectsView(TemplateView):
    template_name = 'main/case-studies/utility-projects.html'

class ContactView(TemplateView):
    template_name = 'main/contact.html'

class ContactBookConsultationView(TemplateView):
    template_name = 'main/contact/book-consultation.html'

class ContactGetQuoteView(TemplateView):
    template_name = 'main/contact/get-quote.html'

class ContactOfficeLocationsView(TemplateView):
    template_name = 'main/contact/office-locations.html'

class ContactRequestDemoView(TemplateView):
    template_name = 'main/contact/request-demo.html'

class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hero_slides'] = json.dumps([
            {
                "image": resolve_static('main/images/Hero-Section/Sam 10LH website image 2.png'),
                "title": "Samrudhhi 10LH",
                "description": "Improve farm productivity with the Samrudhhi-10LH agriculture spraying drone. Designed for efficient pesticide and nutrient application across different crops.",
                "ctaLabel": "Get in Touch",
                "ctaHref": reverse('main:contact'),
            },
            {
                "image": resolve_static('main/images/Website Hero Images/Flycra 2.0 Hero img.png'),
                "title": "Flycra 2.0",
                "description": "Flycra 2.0 helps capture accurate aerial data for mapping, inspections, surveying, and surveillance across industrial and commercial projects.",
                "ctaLabel": "View Products",
                "ctaHref": reverse('main:products-flycra-20'),
            },
            {
                "image": resolve_static('main/images/Website Hero Images/Flyura drone.png'),
                "title": "Flyura",
                "description": "Flyura is designed for surveillance across defence and critical infrastructure. Equipped with EO/IR imaging, laser rangefinder, and AI target detection.",
                "ctaLabel": "Learn More",
                "ctaHref": reverse('main:products-flyura'),
            },
            {
                "image": resolve_static('main/images/Website Hero Images/Uday 1.6 (2).png'),
                "title": "Uday 1.6",
                "description": "UDAY 1.6 compact surveillance and intelligent drone. High-resolution aerial imaging and coverage for defence operations, border security, and infrastructure assessment.",
                "ctaLabel": "Contact Us",
                "ctaHref": reverse('main:contact'),
            },
        ])
        context['product_slides'] = [
            {
                "title": "Samrudhhi-10LH",
                "tagline": "Heavy Lift Hybrid",
                "slug": "samrudhhi-10lh",
                "description": "Built for large-scale farming, it allows for more effective crop spraying and coverage.",
                "image": resolve_static('main/images/products/Sam_10LH/SAM_10LH.png'),
                "href": reverse('main:products-samrudhhi-10lh'),
                "specs": [
                    {"value": "31.5 Kg", "label": "MTOW"},
                    {"value": "10 L", "label": "Tank Capacity"},
                    {"value": "24 min", "label": "Flight Time"},
                ],
            },
            {
                "title": "Flycra 2.0",
                "tagline": "Mapping",
                "slug": "flycra-20",
                "description": "A high-performance mapping drone that delivers sub-centimeter accuracy. Ideal for GIS surveys, construction monitoring, and infrastructure inspection.",
                "image": resolve_static('main/images/products/Flycra 2.0/Flycra 2.0 (front view).png'),
                "href": reverse('main:products-flycra-20'),
                "specs": [
                    {"value": "Upto 2Km", "label": "Range"},
                    {"value": "50 min", "label": "Flight Time"},
                    {"value": "2.4 Kg", "label": "MTOW"},
                ],
            },
            {
                "title": "Nitya FC",
                "tagline": "Flight Controller",
                "slug": "nitya-fc",
                "description": "An indigenous flight controller that provides unprecedented stability and interoperability with our own AI analytics platforms.",
                "image": resolve_static('main/images/products/nitya-fc/Nitya FC.png'),
                "href": reverse('main:products-nitya-fc'),
                "specs": [
                    {"value": "STM32H7 microcontroller @ 480 MHz with FPU", "label": "Processor"},
                    {"value": "FRAM & EEPROM", "label": "Storage"},
                    {"value": "Real-Time OS with failsafe and watchdog routines", "label": "Operating System"},
                ],
            },
            {
                "title": "Flyura",
                "tagline": "Surveillance",
                "slug": "flyura",
                "description": "Advanced surveillance UAV designed for defense and critical infrastructure monitoring with EO/IR imaging and AI target detection.",
                "image": resolve_static('main/images/products/Flyura images/ChatGPT Image Jul 24, 2026, 11_48_49 AM.png'),
                "href": reverse('main:products-flyura'),
                "specs": [
                    {"value": "25 km", "label": "Range"},
                    {"value": "120 min", "label": "Flight Time"},
                    {"value": "15 Kg", "label": "MTOW"},
                ],
            },
            {
                "title": "Uday 1.6",
                "tagline": "Tactical",
                "slug": "uday-16",
                "description": "Compact tactical quadcopter built for rapid deployment, real-time reconnaissance, and reliable aerial surveillance.",
                "image": resolve_static('main/images/products/Uday 1.6/P1, Uday.png'),
                "href": reverse('main:products-uday-16'),
                "specs": [
                    {"value": "30 min", "label": "Flight Time"},
                    {"value": "1.6 kg", "label": "MTOW"},
                    {"value": "4K / 6\u00d7 Zoom", "label": "Camera"},
                ],
            },
        ]
        context['testimonials'] = [
            {
                "quote": "Aeronica delivered exceptional precision in their GIS mapping for our railway corridor project. The sub-centimeter accuracy and detailed terrain analysis exceeded our expectations.",
                "name": "Chief Engineer",
                "role": "Central Railway",
            },
            {
                "quote": "The volumetric analysis from Aeronica's mine survey gave us stockpile numbers we could rely on for planning and reconciliation — far more consistent than our manual methods.",
                "name": "Survey Head",
                "role": "JSW Steel",
            },
            {
                "quote": "Aeronica's pipeline surveillance drones monitored our right-of-way continuously and flagged anomalies in real time, protecting critical infrastructure with minimal ground patrols.",
                "name": "Operations Director",
                "role": "IOCL",
            },
            {
                "quote": "From crop health mapping to spraying operations, Aeronica's agriculture drones have measurably improved how our farmers manage fields and input costs.",
                "name": "Programme Lead",
                "role": "Agriculture Department",
            },
        ]
        return context

class IndustriesView(TemplateView):
    template_name = 'main/industries.html'

class IndustriesAgricultureView(TemplateView):
    template_name = 'main/industries/agriculture.html'

class IndustriesConstructionView(TemplateView):
    template_name = 'main/industries/construction.html'

class IndustriesEnergyView(TemplateView):
    template_name = 'main/industries/energy.html'

class IndustriesGovernmentView(TemplateView):
    template_name = 'main/industries/government.html'

class IndustriesMiningView(TemplateView):
    template_name = 'main/industries/mining.html'

class IndustriesRealEstateView(TemplateView):
    template_name = 'main/industries/real-estate.html'

class IndustriesSmartCitiesView(TemplateView):
    template_name = 'main/industries/smart-cities.html'

class IndustriesTelecomView(TemplateView):
    template_name = 'main/industries/telecom.html'

class IndustriesTransportationView(TemplateView):
    template_name = 'main/industries/transportation.html'

class IndustriesUtilitiesView(TemplateView):
    template_name = 'main/industries/utilities.html'

class LegalView(TemplateView):
    template_name = 'main/legal.html'

class LegalCookiePolicyView(TemplateView):
    template_name = 'main/legal/cookie-policy.html'

class LegalPrivacyPolicyView(TemplateView):
    template_name = 'main/legal/privacy-policy.html'

class LegalRefundPolicyView(TemplateView):
    template_name = 'main/legal/refund-policy.html'

class LegalTermsConditionsView(TemplateView):
    template_name = 'main/legal/terms-conditions.html'

class PartnersBecomeView(TemplateView):
    template_name = 'main/partners/become.html'

class ProductsView(TemplateView):
    template_name = 'main/products.html'

class ProductsFlycra20View(TemplateView):
    template_name = 'main/products/flycra-20.html'

class ProductsFlyuraView(TemplateView):
    template_name = 'main/products/flyura.html'

class ProductsNityaFcView(TemplateView):
    template_name = 'main/products/nitya-fc.html'

class ProductsSamrudhhi10lView(TemplateView):
    template_name = 'main/products/samrudhhi-10l.html'

class ProductsSamrudhhi10lhView(TemplateView):
    template_name = 'main/products/samrudhhi-10lh.html'

class ProductsUday16View(TemplateView):
    template_name = 'main/products/uday-16.html'

class ResearchView(TemplateView):
    template_name = 'main/research.html'

class ResourcesView(TemplateView):
    template_name = 'main/resources.html'

class ResourcesBlogView(TemplateView):
    template_name = 'main/resources/blog.html'

class ResourcesBlogAeronicaReceivesDgcaTypeCertificationForSamrudhhi10lView(TemplateView):
    template_name = 'main/resources/blog/aeronica-receives-dgca-type-certification-for-samrudhhi-10l.html'

class ResourcesBlogAiBasedCropHealthClassificationView(TemplateView):
    template_name = 'main/resources/blog/ai-based-crop-health-classification.html'

class ResourcesBlogAirspaceAuthorizationsView(TemplateView):
    template_name = 'main/resources/blog/airspace-authorizations.html'

class ResourcesBlogBusinessStandardAeronicaFeatureView(TemplateView):
    template_name = 'main/resources/blog/business-standard-aeronica-feature.html'

class ResourcesBlogCompositeAirframeDesignForAgriculturalUavsView(TemplateView):
    template_name = 'main/resources/blog/composite-airframe-design-for-agricultural-uavs.html'

class ResourcesBlogDgcaComplianceGuideView(TemplateView):
    template_name = 'main/resources/blog/dgca-compliance-guide.html'

class ResourcesBlogDigitalSkyPlatformView(TemplateView):
    template_name = 'main/resources/blog/digital-sky-platform.html'

class ResourcesBlogDroneBasedPipelineSurveillanceView(TemplateView):
    template_name = 'main/resources/blog/drone-based-pipeline-surveillance.html'

class ResourcesBlogDroneRules2021Amended2025View(TemplateView):
    template_name = 'main/resources/blog/drone-rules-2021-amended-2025.html'

class ResourcesBlogExpansionOfRdFacilityInPuneView(TemplateView):
    template_name = 'main/resources/blog/expansion-of-rd-facility-in-pune.html'

class ResourcesBlogInsuranceRequirementsView(TemplateView):
    template_name = 'main/resources/blog/insurance-requirements.html'

class ResourcesBlogMineVolumetricAnalysisJswSteelView(TemplateView):
    template_name = 'main/resources/blog/mine-volumetric-analysis-jsw-steel.html'

class ResourcesBlogPartnershipWithIitBombayForAiResearchView(TemplateView):
    template_name = 'main/resources/blog/partnership-with-iit-bombay-for-ai-research.html'

class ResourcesBlogPayloadAndWeightClassificationsView(TemplateView):
    template_name = 'main/resources/blog/payload-and-weight-classifications.html'

class ResourcesBlogPipelineSurveillanceIoclView(TemplateView):
    template_name = 'main/resources/blog/pipeline-surveillance-iocl.html'

class ResourcesBlogPrecisionAgricultureIn2026View(TemplateView):
    template_name = 'main/resources/blog/precision-agriculture-in-2026.html'

class ResourcesBlogRailwayCorridorMappingCentralRailwayView(TemplateView):
    template_name = 'main/resources/blog/railway-corridor-mapping-central-railway.html'

class ResourcesBlogRemotePilotLicenseRplView(TemplateView):
    template_name = 'main/resources/blog/remote-pilot-license-rpl.html'

class ResourcesBlogSecureTelemetryProtocolsForDroneOperationsView(TemplateView):
    template_name = 'main/resources/blog/secure-telemetry-protocols-for-drone-operations.html'

class ResourcesBlogSensorFusionForPrecisionMappingView(TemplateView):
    template_name = 'main/resources/blog/sensor-fusion-for-precision-mapping.html'

class ResourcesBlogTheEconomicTimesAeronicaFeatureView(TemplateView):
    template_name = 'main/resources/blog/the-economic-times-aeronica-feature.html'

class ResourcesBlogTheFutureOfLidarSurveyingView(TemplateView):
    template_name = 'main/resources/blog/the-future-of-lidar-surveying.html'

class ResourcesBlogTypeCertificationProcessView(TemplateView):
    template_name = 'main/resources/blog/type-certification-process.html'

class ResourcesBlogWhyIndigenousFlightControllersMatterView(TemplateView):
    template_name = 'main/resources/blog/why-indigenous-flight-controllers-matter.html'

class ResourcesBlogYourstoryAeronicaFeatureView(TemplateView):
    template_name = 'main/resources/blog/yourstory-aeronica-feature.html'

class ResourcesDownloadsView(TemplateView):
    template_name = 'main/resources/downloads.html'

class ResourcesDownloadsAeronicaReceivesDgcaTypeCertificationForSamrudhhi10lView(TemplateView):
    template_name = 'main/resources/downloads/aeronica-receives-dgca-type-certification-for-samrudhhi-10l.html'

class ResourcesDownloadsAiBasedCropHealthClassificationView(TemplateView):
    template_name = 'main/resources/downloads/ai-based-crop-health-classification.html'

class ResourcesDownloadsAirspaceAuthorizationsView(TemplateView):
    template_name = 'main/resources/downloads/airspace-authorizations.html'

class ResourcesDownloadsBusinessStandardAeronicaFeatureView(TemplateView):
    template_name = 'main/resources/downloads/business-standard-aeronica-feature.html'

class ResourcesDownloadsCompositeAirframeDesignForAgriculturalUavsView(TemplateView):
    template_name = 'main/resources/downloads/composite-airframe-design-for-agricultural-uavs.html'

class ResourcesDownloadsDgcaComplianceGuideView(TemplateView):
    template_name = 'main/resources/downloads/dgca-compliance-guide.html'

class ResourcesDownloadsDigitalSkyPlatformView(TemplateView):
    template_name = 'main/resources/downloads/digital-sky-platform.html'

class ResourcesDownloadsDroneBasedPipelineSurveillanceView(TemplateView):
    template_name = 'main/resources/downloads/drone-based-pipeline-surveillance.html'

class ResourcesDownloadsDroneRules2021Amended2025View(TemplateView):
    template_name = 'main/resources/downloads/drone-rules-2021-amended-2025.html'

class ResourcesDownloadsExpansionOfRdFacilityInPuneView(TemplateView):
    template_name = 'main/resources/downloads/expansion-of-rd-facility-in-pune.html'

class ResourcesDownloadsInsuranceRequirementsView(TemplateView):
    template_name = 'main/resources/downloads/insurance-requirements.html'

class ResourcesDownloadsMineVolumetricAnalysisJswSteelView(TemplateView):
    template_name = 'main/resources/downloads/mine-volumetric-analysis-jsw-steel.html'

class ResourcesDownloadsPartnershipWithIitBombayForAiResearchView(TemplateView):
    template_name = 'main/resources/downloads/partnership-with-iit-bombay-for-ai-research.html'

class ResourcesDownloadsPayloadAndWeightClassificationsView(TemplateView):
    template_name = 'main/resources/downloads/payload-and-weight-classifications.html'

class ResourcesDownloadsPipelineSurveillanceIoclView(TemplateView):
    template_name = 'main/resources/downloads/pipeline-surveillance-iocl.html'

class ResourcesDownloadsPrecisionAgricultureIn2026View(TemplateView):
    template_name = 'main/resources/downloads/precision-agriculture-in-2026.html'

class ResourcesDownloadsRailwayCorridorMappingCentralRailwayView(TemplateView):
    template_name = 'main/resources/downloads/railway-corridor-mapping-central-railway.html'

class ResourcesDownloadsRemotePilotLicenseRplView(TemplateView):
    template_name = 'main/resources/downloads/remote-pilot-license-rpl.html'

class ResourcesDownloadsSecureTelemetryProtocolsForDroneOperationsView(TemplateView):
    template_name = 'main/resources/downloads/secure-telemetry-protocols-for-drone-operations.html'

class ResourcesDownloadsSensorFusionForPrecisionMappingView(TemplateView):
    template_name = 'main/resources/downloads/sensor-fusion-for-precision-mapping.html'

class ResourcesDownloadsTheEconomicTimesAeronicaFeatureView(TemplateView):
    template_name = 'main/resources/downloads/the-economic-times-aeronica-feature.html'

class ResourcesDownloadsTheFutureOfLidarSurveyingView(TemplateView):
    template_name = 'main/resources/downloads/the-future-of-lidar-surveying.html'

class ResourcesDownloadsTypeCertificationProcessView(TemplateView):
    template_name = 'main/resources/downloads/type-certification-process.html'

class ResourcesDownloadsWhyIndigenousFlightControllersMatterView(TemplateView):
    template_name = 'main/resources/downloads/why-indigenous-flight-controllers-matter.html'

class ResourcesDownloadsYourstoryAeronicaFeatureView(TemplateView):
    template_name = 'main/resources/downloads/yourstory-aeronica-feature.html'

class ResourcesDroneRegulationsView(TemplateView):
    template_name = 'main/resources/drone-regulations.html'

class ResourcesDroneRegulationsAeronicaReceivesDgcaTypeCertificationForSamrudhhi10lView(TemplateView):
    template_name = 'main/resources/drone-regulations/aeronica-receives-dgca-type-certification-for-samrudhhi-10l.html'

class ResourcesDroneRegulationsAiBasedCropHealthClassificationView(TemplateView):
    template_name = 'main/resources/drone-regulations/ai-based-crop-health-classification.html'

class ResourcesDroneRegulationsAirspaceAuthorizationsView(TemplateView):
    template_name = 'main/resources/drone-regulations/airspace-authorizations.html'

class ResourcesDroneRegulationsBusinessStandardAeronicaFeatureView(TemplateView):
    template_name = 'main/resources/drone-regulations/business-standard-aeronica-feature.html'

class ResourcesDroneRegulationsCompositeAirframeDesignForAgriculturalUavsView(TemplateView):
    template_name = 'main/resources/drone-regulations/composite-airframe-design-for-agricultural-uavs.html'

class ResourcesDroneRegulationsDgcaComplianceGuideView(TemplateView):
    template_name = 'main/resources/drone-regulations/dgca-compliance-guide.html'

class ResourcesDroneRegulationsDigitalSkyPlatformView(TemplateView):
    template_name = 'main/resources/drone-regulations/digital-sky-platform.html'

class ResourcesDroneRegulationsDroneBasedPipelineSurveillanceView(TemplateView):
    template_name = 'main/resources/drone-regulations/drone-based-pipeline-surveillance.html'

class ResourcesDroneRegulationsDroneRules2021Amended2025View(TemplateView):
    template_name = 'main/resources/drone-regulations/drone-rules-2021-amended-2025.html'

class ResourcesDroneRegulationsExpansionOfRdFacilityInPuneView(TemplateView):
    template_name = 'main/resources/drone-regulations/expansion-of-rd-facility-in-pune.html'

class ResourcesDroneRegulationsInsuranceRequirementsView(TemplateView):
    template_name = 'main/resources/drone-regulations/insurance-requirements.html'

class ResourcesDroneRegulationsMineVolumetricAnalysisJswSteelView(TemplateView):
    template_name = 'main/resources/drone-regulations/mine-volumetric-analysis-jsw-steel.html'

class ResourcesDroneRegulationsPartnershipWithIitBombayForAiResearchView(TemplateView):
    template_name = 'main/resources/drone-regulations/partnership-with-iit-bombay-for-ai-research.html'

class ResourcesDroneRegulationsPayloadAndWeightClassificationsView(TemplateView):
    template_name = 'main/resources/drone-regulations/payload-and-weight-classifications.html'

class ResourcesDroneRegulationsPipelineSurveillanceIoclView(TemplateView):
    template_name = 'main/resources/drone-regulations/pipeline-surveillance-iocl.html'

class ResourcesDroneRegulationsPrecisionAgricultureIn2026View(TemplateView):
    template_name = 'main/resources/drone-regulations/precision-agriculture-in-2026.html'

class ResourcesDroneRegulationsRailwayCorridorMappingCentralRailwayView(TemplateView):
    template_name = 'main/resources/drone-regulations/railway-corridor-mapping-central-railway.html'

class ResourcesDroneRegulationsRemotePilotLicenseRplView(TemplateView):
    template_name = 'main/resources/drone-regulations/remote-pilot-license-rpl.html'

class ResourcesDroneRegulationsSecureTelemetryProtocolsForDroneOperationsView(TemplateView):
    template_name = 'main/resources/drone-regulations/secure-telemetry-protocols-for-drone-operations.html'

class ResourcesDroneRegulationsSensorFusionForPrecisionMappingView(TemplateView):
    template_name = 'main/resources/drone-regulations/sensor-fusion-for-precision-mapping.html'

class ResourcesDroneRegulationsTheEconomicTimesAeronicaFeatureView(TemplateView):
    template_name = 'main/resources/drone-regulations/the-economic-times-aeronica-feature.html'

class ResourcesDroneRegulationsTheFutureOfLidarSurveyingView(TemplateView):
    template_name = 'main/resources/drone-regulations/the-future-of-lidar-surveying.html'

class ResourcesDroneRegulationsTypeCertificationProcessView(TemplateView):
    template_name = 'main/resources/drone-regulations/type-certification-process.html'

class ResourcesDroneRegulationsWhyIndigenousFlightControllersMatterView(TemplateView):
    template_name = 'main/resources/drone-regulations/why-indigenous-flight-controllers-matter.html'

class ResourcesDroneRegulationsYourstoryAeronicaFeatureView(TemplateView):
    template_name = 'main/resources/drone-regulations/yourstory-aeronica-feature.html'

class ResourcesFaqsView(TemplateView):
    template_name = 'main/resources/faqs.html'

class ResourcesFaqsAeronicaReceivesDgcaTypeCertificationForSamrudhhi10lView(TemplateView):
    template_name = 'main/resources/faqs/aeronica-receives-dgca-type-certification-for-samrudhhi-10l.html'

class ResourcesFaqsAiBasedCropHealthClassificationView(TemplateView):
    template_name = 'main/resources/faqs/ai-based-crop-health-classification.html'

class ResourcesFaqsAirspaceAuthorizationsView(TemplateView):
    template_name = 'main/resources/faqs/airspace-authorizations.html'

class ResourcesFaqsBusinessStandardAeronicaFeatureView(TemplateView):
    template_name = 'main/resources/faqs/business-standard-aeronica-feature.html'

class ResourcesFaqsCompositeAirframeDesignForAgriculturalUavsView(TemplateView):
    template_name = 'main/resources/faqs/composite-airframe-design-for-agricultural-uavs.html'

class ResourcesFaqsDgcaComplianceGuideView(TemplateView):
    template_name = 'main/resources/faqs/dgca-compliance-guide.html'

class ResourcesFaqsDigitalSkyPlatformView(TemplateView):
    template_name = 'main/resources/faqs/digital-sky-platform.html'

class ResourcesFaqsDroneBasedPipelineSurveillanceView(TemplateView):
    template_name = 'main/resources/faqs/drone-based-pipeline-surveillance.html'

class ResourcesFaqsDroneRules2021Amended2025View(TemplateView):
    template_name = 'main/resources/faqs/drone-rules-2021-amended-2025.html'

class ResourcesFaqsExpansionOfRdFacilityInPuneView(TemplateView):
    template_name = 'main/resources/faqs/expansion-of-rd-facility-in-pune.html'

class ResourcesFaqsInsuranceRequirementsView(TemplateView):
    template_name = 'main/resources/faqs/insurance-requirements.html'

class ResourcesFaqsMineVolumetricAnalysisJswSteelView(TemplateView):
    template_name = 'main/resources/faqs/mine-volumetric-analysis-jsw-steel.html'

class ResourcesFaqsPartnershipWithIitBombayForAiResearchView(TemplateView):
    template_name = 'main/resources/faqs/partnership-with-iit-bombay-for-ai-research.html'

class ResourcesFaqsPayloadAndWeightClassificationsView(TemplateView):
    template_name = 'main/resources/faqs/payload-and-weight-classifications.html'

class ResourcesFaqsPipelineSurveillanceIoclView(TemplateView):
    template_name = 'main/resources/faqs/pipeline-surveillance-iocl.html'

class ResourcesFaqsPrecisionAgricultureIn2026View(TemplateView):
    template_name = 'main/resources/faqs/precision-agriculture-in-2026.html'

class ResourcesFaqsRailwayCorridorMappingCentralRailwayView(TemplateView):
    template_name = 'main/resources/faqs/railway-corridor-mapping-central-railway.html'

class ResourcesFaqsRemotePilotLicenseRplView(TemplateView):
    template_name = 'main/resources/faqs/remote-pilot-license-rpl.html'

class ResourcesFaqsSecureTelemetryProtocolsForDroneOperationsView(TemplateView):
    template_name = 'main/resources/faqs/secure-telemetry-protocols-for-drone-operations.html'

class ResourcesFaqsSensorFusionForPrecisionMappingView(TemplateView):
    template_name = 'main/resources/faqs/sensor-fusion-for-precision-mapping.html'

class ResourcesFaqsTheEconomicTimesAeronicaFeatureView(TemplateView):
    template_name = 'main/resources/faqs/the-economic-times-aeronica-feature.html'

class ResourcesFaqsTheFutureOfLidarSurveyingView(TemplateView):
    template_name = 'main/resources/faqs/the-future-of-lidar-surveying.html'

class ResourcesFaqsTypeCertificationProcessView(TemplateView):
    template_name = 'main/resources/faqs/type-certification-process.html'

class ResourcesFaqsWhyIndigenousFlightControllersMatterView(TemplateView):
    template_name = 'main/resources/faqs/why-indigenous-flight-controllers-matter.html'

class ResourcesFaqsYourstoryAeronicaFeatureView(TemplateView):
    template_name = 'main/resources/faqs/yourstory-aeronica-feature.html'

class ResourcesNewsMediaView(TemplateView):
    template_name = 'main/resources/news-media.html'

class ResourcesNewsMediaAeronicaReceivesDgcaTypeCertificationForSamrudhhi10lView(TemplateView):
    template_name = 'main/resources/news-media/aeronica-receives-dgca-type-certification-for-samrudhhi-10l.html'

class ResourcesNewsMediaAiBasedCropHealthClassificationView(TemplateView):
    template_name = 'main/resources/news-media/ai-based-crop-health-classification.html'

class ResourcesNewsMediaAirspaceAuthorizationsView(TemplateView):
    template_name = 'main/resources/news-media/airspace-authorizations.html'

class ResourcesNewsMediaBusinessStandardAeronicaFeatureView(TemplateView):
    template_name = 'main/resources/news-media/business-standard-aeronica-feature.html'

class ResourcesNewsMediaCompositeAirframeDesignForAgriculturalUavsView(TemplateView):
    template_name = 'main/resources/news-media/composite-airframe-design-for-agricultural-uavs.html'

class ResourcesNewsMediaDgcaComplianceGuideView(TemplateView):
    template_name = 'main/resources/news-media/dgca-compliance-guide.html'

class ResourcesNewsMediaDigitalSkyPlatformView(TemplateView):
    template_name = 'main/resources/news-media/digital-sky-platform.html'

class ResourcesNewsMediaDroneBasedPipelineSurveillanceView(TemplateView):
    template_name = 'main/resources/news-media/drone-based-pipeline-surveillance.html'

class ResourcesNewsMediaDroneRules2021Amended2025View(TemplateView):
    template_name = 'main/resources/news-media/drone-rules-2021-amended-2025.html'

class ResourcesNewsMediaExpansionOfRdFacilityInPuneView(TemplateView):
    template_name = 'main/resources/news-media/expansion-of-rd-facility-in-pune.html'

class ResourcesNewsMediaInsuranceRequirementsView(TemplateView):
    template_name = 'main/resources/news-media/insurance-requirements.html'

class ResourcesNewsMediaMineVolumetricAnalysisJswSteelView(TemplateView):
    template_name = 'main/resources/news-media/mine-volumetric-analysis-jsw-steel.html'

class ResourcesNewsMediaPartnershipWithIitBombayForAiResearchView(TemplateView):
    template_name = 'main/resources/news-media/partnership-with-iit-bombay-for-ai-research.html'

class ResourcesNewsMediaPayloadAndWeightClassificationsView(TemplateView):
    template_name = 'main/resources/news-media/payload-and-weight-classifications.html'

class ResourcesNewsMediaPipelineSurveillanceIoclView(TemplateView):
    template_name = 'main/resources/news-media/pipeline-surveillance-iocl.html'

class ResourcesNewsMediaPrecisionAgricultureIn2026View(TemplateView):
    template_name = 'main/resources/news-media/precision-agriculture-in-2026.html'

class ResourcesNewsMediaRailwayCorridorMappingCentralRailwayView(TemplateView):
    template_name = 'main/resources/news-media/railway-corridor-mapping-central-railway.html'

class ResourcesNewsMediaRemotePilotLicenseRplView(TemplateView):
    template_name = 'main/resources/news-media/remote-pilot-license-rpl.html'

class ResourcesNewsMediaSecureTelemetryProtocolsForDroneOperationsView(TemplateView):
    template_name = 'main/resources/news-media/secure-telemetry-protocols-for-drone-operations.html'

class ResourcesNewsMediaSensorFusionForPrecisionMappingView(TemplateView):
    template_name = 'main/resources/news-media/sensor-fusion-for-precision-mapping.html'

class ResourcesNewsMediaTheEconomicTimesAeronicaFeatureView(TemplateView):
    template_name = 'main/resources/news-media/the-economic-times-aeronica-feature.html'

class ResourcesNewsMediaTheFutureOfLidarSurveyingView(TemplateView):
    template_name = 'main/resources/news-media/the-future-of-lidar-surveying.html'

class ResourcesNewsMediaTypeCertificationProcessView(TemplateView):
    template_name = 'main/resources/news-media/type-certification-process.html'

class ResourcesNewsMediaWhyIndigenousFlightControllersMatterView(TemplateView):
    template_name = 'main/resources/news-media/why-indigenous-flight-controllers-matter.html'

class ResourcesNewsMediaYourstoryAeronicaFeatureView(TemplateView):
    template_name = 'main/resources/news-media/yourstory-aeronica-feature.html'

class ResourcesWhitepapersView(TemplateView):
    template_name = 'main/resources/whitepapers.html'

class ResourcesWhitepapersAeronicaReceivesDgcaTypeCertificationForSamrudhhi10lView(TemplateView):
    template_name = 'main/resources/whitepapers/aeronica-receives-dgca-type-certification-for-samrudhhi-10l.html'

class ResourcesWhitepapersAiBasedCropHealthClassificationView(TemplateView):
    template_name = 'main/resources/whitepapers/ai-based-crop-health-classification.html'

class ResourcesWhitepapersAirspaceAuthorizationsView(TemplateView):
    template_name = 'main/resources/whitepapers/airspace-authorizations.html'

class ResourcesWhitepapersBusinessStandardAeronicaFeatureView(TemplateView):
    template_name = 'main/resources/whitepapers/business-standard-aeronica-feature.html'

class ResourcesWhitepapersCompositeAirframeDesignForAgriculturalUavsView(TemplateView):
    template_name = 'main/resources/whitepapers/composite-airframe-design-for-agricultural-uavs.html'

class ResourcesWhitepapersDgcaComplianceGuideView(TemplateView):
    template_name = 'main/resources/whitepapers/dgca-compliance-guide.html'

class ResourcesWhitepapersDigitalSkyPlatformView(TemplateView):
    template_name = 'main/resources/whitepapers/digital-sky-platform.html'

class ResourcesWhitepapersDroneBasedPipelineSurveillanceView(TemplateView):
    template_name = 'main/resources/whitepapers/drone-based-pipeline-surveillance.html'

class ResourcesWhitepapersDroneRules2021Amended2025View(TemplateView):
    template_name = 'main/resources/whitepapers/drone-rules-2021-amended-2025.html'

class ResourcesWhitepapersExpansionOfRdFacilityInPuneView(TemplateView):
    template_name = 'main/resources/whitepapers/expansion-of-rd-facility-in-pune.html'

class ResourcesWhitepapersInsuranceRequirementsView(TemplateView):
    template_name = 'main/resources/whitepapers/insurance-requirements.html'

class ResourcesWhitepapersMineVolumetricAnalysisJswSteelView(TemplateView):
    template_name = 'main/resources/whitepapers/mine-volumetric-analysis-jsw-steel.html'

class ResourcesWhitepapersPartnershipWithIitBombayForAiResearchView(TemplateView):
    template_name = 'main/resources/whitepapers/partnership-with-iit-bombay-for-ai-research.html'

class ResourcesWhitepapersPayloadAndWeightClassificationsView(TemplateView):
    template_name = 'main/resources/whitepapers/payload-and-weight-classifications.html'

class ResourcesWhitepapersPipelineSurveillanceIoclView(TemplateView):
    template_name = 'main/resources/whitepapers/pipeline-surveillance-iocl.html'

class ResourcesWhitepapersPrecisionAgricultureIn2026View(TemplateView):
    template_name = 'main/resources/whitepapers/precision-agriculture-in-2026.html'

class ResourcesWhitepapersRailwayCorridorMappingCentralRailwayView(TemplateView):
    template_name = 'main/resources/whitepapers/railway-corridor-mapping-central-railway.html'

class ResourcesWhitepapersRemotePilotLicenseRplView(TemplateView):
    template_name = 'main/resources/whitepapers/remote-pilot-license-rpl.html'

class ResourcesWhitepapersSecureTelemetryProtocolsForDroneOperationsView(TemplateView):
    template_name = 'main/resources/whitepapers/secure-telemetry-protocols-for-drone-operations.html'

class ResourcesWhitepapersSensorFusionForPrecisionMappingView(TemplateView):
    template_name = 'main/resources/whitepapers/sensor-fusion-for-precision-mapping.html'

class ResourcesWhitepapersTheEconomicTimesAeronicaFeatureView(TemplateView):
    template_name = 'main/resources/whitepapers/the-economic-times-aeronica-feature.html'

class ResourcesWhitepapersTheFutureOfLidarSurveyingView(TemplateView):
    template_name = 'main/resources/whitepapers/the-future-of-lidar-surveying.html'

class ResourcesWhitepapersTypeCertificationProcessView(TemplateView):
    template_name = 'main/resources/whitepapers/type-certification-process.html'

class ResourcesWhitepapersWhyIndigenousFlightControllersMatterView(TemplateView):
    template_name = 'main/resources/whitepapers/why-indigenous-flight-controllers-matter.html'

class ResourcesWhitepapersYourstoryAeronicaFeatureView(TemplateView):
    template_name = 'main/resources/whitepapers/yourstory-aeronica-feature.html'

class SeoDigitalTwinServicesView(TemplateView):
    template_name = 'main/seo/digital-twin-services.html'

class SeoDroneInspectionServicesView(TemplateView):
    template_name = 'main/seo/drone-inspection-services.html'

class SeoDroneSurveyCompanyPuneView(TemplateView):
    template_name = 'main/seo/drone-survey-company-pune.html'

class SeoDroneSurveyMaharashtraView(TemplateView):
    template_name = 'main/seo/drone-survey-maharashtra.html'

class SeoGisSolutionsIndiaView(TemplateView):
    template_name = 'main/seo/gis-solutions-india.html'

class SeoHighwayMappingServicesView(TemplateView):
    template_name = 'main/seo/highway-mapping-services.html'

class SeoLidarSurveyServicesIndiaView(TemplateView):
    template_name = 'main/seo/lidar-survey-services-india.html'

class SeoMiningDroneSurveyView(TemplateView):
    template_name = 'main/seo/mining-drone-survey.html'

class SeoSolarPlantInspectionView(TemplateView):
    template_name = 'main/seo/solar-plant-inspection.html'

class SitemapView(TemplateView):
    template_name = 'main/sitemap.html'

class SolutionsView(TemplateView):
    template_name = 'main/solutions.html'

class SolutionsAiDroneIntelligenceView(TemplateView):
    template_name = 'main/solutions/ai-drone-intelligence.html'

class SolutionsDisasterEmergencyResponseView(TemplateView):
    template_name = 'main/solutions/disaster-emergency-response.html'

class SolutionsDroneSurveyMappingView(TemplateView):
    template_name = 'main/solutions/drone-survey-mapping.html'

class SolutionsGisGeospatialIntelligenceView(TemplateView):
    template_name = 'main/solutions/gis-geospatial-intelligence.html'

class SolutionsInfrastructureInspectionView(TemplateView):
    template_name = 'main/solutions/infrastructure-inspection.html'
