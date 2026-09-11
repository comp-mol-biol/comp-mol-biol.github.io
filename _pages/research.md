---
permalink: /research/
title: "Research"
layout: single
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

Our group investigates how dynamic self-organization gives rise to specific regulation in cells. Self-organization is ubiquitous in cells and essential for regulating biological processes in time and space. Proteins and nucleic acid fold and interact and self-assembly into large macromolecular complexes. Biomolecules also phase separate to form liquid biomolecular condensates. Notably, phase separation of proteins and specific recruitment of protein-RNA complexes by these phase-separated condensates underpins transgenerational epigenetic inheritance in C. elegans. By contrast, in neurodegenerative diseases such amyotrophic lateral sclerosis (ALS), frontotemporal dementia (FTD), and Alzheimer’s disease phase separation is implicated in the formation of toxic aggregates. Liquid condensates, which have important functional roles, “age” on the molecular level and undergo a liquid to solid transition which results in toxic aggregates. Dysregulation of phase separation as cells age and the consequential formation of toxic aggregates may even be a general driver of aging.  

We are using multi-scale molecular dynamics simulations (Fig 1) and machine learning to study intrinsically disordered and folded proteins, the effects of post-translational modifications on proteins, as well as protein-DNA and protein-RNA interactions. Cell rely fundamentally on chemical fuel (e.g. ATP) driven non-equilibrium processes and including such chemical-driven reactions in simulation models will aid our understanding of organization of biomolecules at the subcellular level. Simulations also help us to understand synthetic systems, which can aid our understanding of regulatory principles in cells. Our research is broadly organised along four research lines: 1) Phase separation of RNA binding proteins, 2) Multivalent interactions and condensation in transcription 3) Specificity in small interfering RNA pathways 4) Development of multi-scale simulation methods and integration of experiments and simulations. 

<figure>
  <img src="/images/multiscale.png" alt="multiscale simulations" />
  <figcaption>
    Figure 1: Multi-scale simulation framework to investigate phase behavior and molecular
    recognition, combining atomistic, near-atomic (Martini3), and residue-level
    (CALVADOS2) simulations (Gaurav et al., Biophys J 2025).
  </figcaption>
</figure>

## Phase separation of RNA binding proteins

In collaboration with Dorothee Dormann (IMB/JGU), we are studying  TDP-43 phosphorylation (Gruijs da Silva, EMBO J 2022). Phosphorylation of TDP-43 is a hallmark of neurodegenerative disease. The paradigm of the field has been that phosphorylation induces phase separation and pathological aggregation of TDP-43. However, experiments by the Dormann lab suggested that phosphorylation may be a cytoprotective mechanism. Our simulations provide a mechanistic basis for this cytoprotective effect, showing how phosphorylation breaks contacts in the C-terminus of TDP-43. In atomistic simulations we could resolve the consequences of phosphorylation, by using our hierarchical chain growth method to generate starting structures for simulations of TDP-43 low complexity domain (LCD) condensates  (Pietrek*, Stelzl* J Chem Theory Comput 2020). More recently we have studied the phase behaviour of full-length TDP-43 in coarse-grained simulations. Using the Martini3 simulation model we retained a relatively detailed description of the protein, including water and ions. We aim to capture how mutations of aromatic residues, and phospho-mimicking mutations determine phase behavior (Ping, bioRvix 2026). These comprehensive simulations of TDP-43 also highlight that, e.g., interactions of the RRM2 and the C-terminal helix are important and suggest that the nuclear localization sequence and its phosphorylation may modulate TDP-43 phase separation. With these simulations we will investigate the material properties of TDP-43 condensates to better understand how they change in neurodegenerative diseases, where condensates become less liquid and less functional over time.

To better understand the proposed cyto-protective mechanism of TDP-43, we asked how the kinase Ck1δ would interact with TDP-43 (Zippo, Nat Commun 2025), whether Ck1δ would only bind and phosphorylate TDP-43 only in dilute solution or whether Ck1δ can bind and phosphorylate TDP-43 condensates. Combining a Monte Carlo move with molecular dynamics simulations enabled us to simulate how enzymes interact with condensates and to validate the simulation approach we adapted existing Markov-state modeling approaches, which demonstrated that our simulations are thermodynamically consistent. Our simulations show that Ck1δ interacts preferably with the interfaces of TDP-43 and directly phosphorylates TDP-43 condensates which triggers their dissolution (Fig. 2). Many different cellular processes are driven by the dissipation of chemical fuels. Considering that weakening of chemical-fuel driven homeostatic mechanisms may be a driver of the formation of toxic aggregates in neurodegenerative diseases further illustrates the importance of our new approach.  

<figure>
  <img src="/images/research1.png" alt="TDP-43 phosphorylation" />
  <figcaption>
  Figure 2: Enzymatic phosphorylation of TDP-43 by the Casein kinase 1 δ (Ck1δ) can dissolve TDP-43 condensates. Ck1δ in blue. Phosphorylated Ser residues on TDP-43 are shown in red. Ck1δ attaches to TDP-43 condensates and over time phosphorylates these condensates, as evidenced by the accumulation of phosphorylated Ser beads (red beads)
  </figcaption>
</figure>


## Multivalent interactions and condensation in transcription 

Our simulations showed how RNA polymerase II C-terminal domain (CTD) condensates could play a key role in the regulation of the transcription of genes. Unphosphorylated RNA Polymerase II is recruited to promoters, where it gets phosphorylated on Ser5 and then as it enters elongation is phosphorylated on Ser2. It has been hypothesized that condensates of RNA polymerase II and other transcription components support transcription initiation and perhaps even help to demarcate the initiation and elongation phases of transcription. However, how this would happen on the molecular scale has remained elusive. To set the scene, we investigated the structure of disordered CTD in dilute solution in collaboration with the Zweckstetter lab (DZNE). With HCG (Stelzl*,Pietrek*, JACS Au 2022, Pietrek*, Stelzl*, J Chem Theory Comput 2020) we showed how local structure is formed in CTD, e.g., by Tyr-Pro interactions which are also important for the interactions of CTD with the Mediator complex (Flores-David, Nat Commun 2023). Extending our modeling to CTD condensates which might underpin transcription initiation, we found that these Tyr-Pro contacts also contributed to the formation of CTD condensates.  Our simulations predicted that CTD condensates would be more stable at higher than lower temperatures, contrary to most protein condensates. In vivo experiments by the Padeken group are in line with our simulations. Together, these results suggest that CTD forms distinct condensates in nuclei, different from those of other proteins, which helps explain how CTD condensates can regulate specific biological processes (Changiarath, bioRxiv 2024). Changing the RNA polymerase II condensation by small changes in temperature also shifts the gene expression profile of C. elegans embryos without triggering a classical heat shock response, which is consistent with a functional role of RNA polymerase II condensates.  
Our simulations show that phosphorylation of RNA polymerase II CTD leads to partially de-mixing of putative initiation and elongation condensates. We showed in simulations that increasing the phosphorylation level of CTD triggers a partial demixing of CTD phases which could underpin differential recruitment of transcription machinery components for the initiation and elongation phases. In vitro experiments by the Padeken lab also show (partial) demixing of partially phosphorylated and unphosphorylated CTD. At very high phosphorylation levels, as may occur in vivo, the condensates form entirely distinct phases. Intriguingly, the condensate phases remained in contact, with condensates of unphosphorylated CTD being fully and partially engulfed by condensates of phosphorylated CTD and elongation factors. We can explain based on the interfacial tension of the different condensates computed from our simulations. This suggests that even at very high phosphorylation levels initiation and elongation condensates would not be entirely separated as had been proposed but would remain in close contact.  Experiments in C. elegans by Jan Padeken (IMB) show that Ser5 and Ser5 phosphorylated RNA Polymerase II form adjacent and partially overlapping foci in line with our simulations. Taken together our simulations provide an initial molecular picture of how condensation underpins a key process in cell biology.

## Specificity in small interfering RNA pathways

To understand how phase-separation may provide for robust and specific regulation, we are collaborating with R. Ketting (IMB) Mainz, who is studies Arognaute proteins and how they regulate small RNA biology in the model organism C. elegans. Small RNAs are produced in the Mutator focus, which is a membrane-less organelle and considered a biomolecular condensate. Such RNAs are important for transposon silencing, gene regulation, and trans-generational epigenetic inheritance. These RNAs are then loaded onto the Arognaute proteins WAGO-1 and WAGO-3. RNAs loaded to WAGO-3 contribute to trans-generational epigenetic inheritance as WAGO-3 can bind to PEI condensates.

<figure>
  <img src="/images/research2.png" alt="MUT16 MUT8" />
  <figcaption>
  Figure 3: Atomistic simulation of MUT-16 and MUT-8 N-terminal region. (A) Atomistic simulation depicting 100 chains of MUT-16 M8BR (gray) and the N-terminal domain of MUT-8 (orange). Sodium and chloride ions are shown as olive and red points, respectively, suspended in water (blue). For clarity, the water on the right half of the simulation box is deleted. (B) aromatic ring of Tyr and guanidinium group of Arg interacting in the condensate
  </figcaption>
</figure>

The emerging picture from simulations of Mutator foci formation and the interaction of PEI condensates and WAGO proteins and experiments (Ketting lab), is that selective recruitment of disordered regions to condensates are an important factor but not the only factor controlling the subcellular localization of Argonaute proteins. E.g., Mutator condensates need to recruit MUT-8 to generate 22G RNA. Our multiscale simulations revealed with atomic resolution how MUT-18 recruits MUT-8 via MUT-8’s Tyr residues (Fig 3 A,B), which was confirmed by experiments (Gaurav, Biophys J 2025). More recently we have used all-atom simulations to understand the dynamics of MUT-16 (Fig 4), where we quantified the dynamics of individual contacts, which could help us better understand the emergent properties of Mutator foci (Kumar Gaurav bioRxiv 2026). 


<figure>
  <img src="/images/mut16_interactions.jpg" alt="mut16 interactions" />
  <figcaption>
Figure 4: Simulation slab box containing MUT-16 foci-forming region chains, each represented by a distinct color. The protein chains are solvated in water (cyan) with ions, Na+ (red) and Cl− (green). Representative specific interactions observed in the simulation are highlighted, including cation-π interactions between the guanidinium group of Arg and the phenol group of Tyr, π-π stacking between phenol groups of Tyr residues, salt bridges between the guanidinium group of Arg and the side-chain carboxylate group of Glu, and hydrogen bonds between the hydroxyl group of Tyr and the carboxylate group of Glu. (Gaurav et al., eLife 2026).
  </figcaption>
</figure>


Disordered regions also regulate the pathway via auto-inhibition (Fig 5). Atomistic molecular dynamics simulations revealed that WAGO-3 is auto-inhibited by its N-terminal disordered tail (Isolehto bioRxiv 2025). The N-terminal disordered tail must move away for WAGO-3 to be able to bind RNA. Germ cells cannot develop properly when the N-terminus of WAGO-3 is deleted as the wrong RNAs are silenced and the worms are sterile consequently. 

<figure class="figure--small">
  <img src="/images/research3_upscayl_2x_upscayl-standard-4x.png" alt="WAGO 3 IDR tail" />
  <figcaption>
  Figure 5: Disordered tail of WAGO-3 blocks RNA binding site. Adapated from Isoletho bioRxiv 2025
  </figcaption>
</figure>

## Development of multi-scale simulation methods & integration of experiments & simulations

Further development of simulation methods and simulation analysis methods is often necessary to make progress with our biological and biophysical research program. E.g., we developed new methods to resolve residual structures in disordered regions of proteins (Pietrek*,Stelzl* J Chem Theory Comput 2020, Stelzl*, Pietrek* JACS Au 2022). Molecular recognition poses a critical challenge for quantitative simulation methods, where subtle differences, e.g, due to a post-translational modification can have a large impact on protein-protein interactions. Increasingly, neural networks are helping us to find biological important patterns based on our simulations (Changiarath, Faraday Discuss 2025, Kumar Gaurav bioRxiv 2026). Using active learning we were able to learn patterns from simulations of protein self-interaction and co-condensation. In the active learning approach, simulation results test the predictions of the neural network which thus gets feedback. The neural networks we trained enabled us to model the co-condensation with CTD and designing multi-phasic CTD condensates.


